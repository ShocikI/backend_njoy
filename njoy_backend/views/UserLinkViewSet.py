from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from django_postgis.authentication import EncryptedTokenAuthentication
from njoy_backend.permissions import IsOwnerOrReadOnly
from njoy_backend.serializers import ( UserLinkSerializer )
from njoy_backend.models import ( UserLink, User )

class UserLinkViewSet(viewsets.ModelViewSet):
    serializer_class = UserLinkSerializer
    authentication_classes = [EncryptedTokenAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = UserLink.objects.all()
        
    def get_queryset(self):
        username = self.kwargs.get('username_username')
        if username:
            user = get_object_or_404(User, username=username)
            return UserLink.objects.filter(owner=user)
        return UserLink.objects.none()
    
    def perform_create(self, serializer):
        username = self.kwargs.get("username_username")
        user = get_object_or_404(User, username=username)
        serializer.save(owner=user)