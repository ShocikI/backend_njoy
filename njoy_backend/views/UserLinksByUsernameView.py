from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status

from njoy_backend.models import UserLink, User
from njoy_backend.serializers import UserLinkSerializer
from django_postgis.authentication import EncryptedTokenAuthentication


class UserLinkByUsernameView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [EncryptedTokenAuthentication]
    
    def get(self, request, username):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = UserLink.objects.filter(owner=user)
        serializer = UserLinkSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)