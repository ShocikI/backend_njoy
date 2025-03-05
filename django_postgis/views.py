
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

class Logout(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
