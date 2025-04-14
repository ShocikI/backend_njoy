from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from django_postgis.authentication import EncryptedTokenAuthentication
from njoy_backend.serializers import ( UserLinkSerializer, UserLink, User )

class UserLinkViewSet(viewsets.ModelViewSet):
    serializer_class = UserLinkSerializer
    authentication_classes = [EncryptedTokenAuthentication]
    queryset = UserLink.objects.all()

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
        
    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['owner_id'] = request.user.id

        serializer = self.get_serializer(data=data)
        if not serializer.is_valid():
            print(f"[UserLink] Błąd walidacji: {serializer.errors}")
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        serializer.save()