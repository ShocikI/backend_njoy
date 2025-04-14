from rest_framework import viewsets

from njoy_backend.serializers import ( UserLinkSerializer, UserLink )

class UserLinkViewSet(viewsets.ModelViewSet):
    serializer_class = UserLinkSerializer
    queryset = UserLink.objects.all()