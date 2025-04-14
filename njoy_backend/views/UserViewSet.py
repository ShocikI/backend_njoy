from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
import os

from django_postgis.authentication import EncryptedTokenAuthentication

from njoy_backend.serializers import (
    RegistrationSerializer, 
    UserProfileSerializer, 
    UserSerializer,
    User, 
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    authentication_classes = [ EncryptedTokenAuthentication ]
    queryset = User.objects.all()
    lookup_field = 'username'

    def get_serializer_class(self):
        match self.action:
            case 'create':
                return RegistrationSerializer
            case 'list':
                return UserSerializer
            case _:
                return UserProfileSerializer
            
    def get_permissions(self):
        match self.action:
            case 'create' | 'list': 
                return [ permissions.AllowAny() ]
            case _:
                return [ permissions.IsAuthenticated() ]


    def retrieve(self, request, username=None):
        try:
            queryset = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, username=None, *args, **kwargs):
        partial = kwargs.pop('partial', True)

        try:
            queryset = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(None, status=status.HTTP_404_NOT_FOUND)

        allowed_fields = {'avatar', 'description'}
        requested_fields = set(request.data.keys())

        if len(requested_fields) != 1:
            return Response(
                {"detail": "Only one field at one time (avatar lub description)."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if 'avatar' in request.data:
            new_avatar = request.data.get('avatar')
            old_avatar = queryset.avatar
            if new_avatar and old_avatar and hasattr(new_avatar, 'name'):
                if old_avatar.name != new_avatar.name:
                    if hasattr(old_avatar, 'path') and os.path.isfile(old_avatar.path):
                        os.remove(old_avatar.path)

        serializer = self.get_serializer(queryset, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data, status=status.HTTP_200_OK)
