
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .encryption import encrypt_token

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user: 
            token, created = Token.objects.get_or_create(user=user)
            encrypted_token = encrypt_token(token.key)
            return Response({"token": encrypted_token })

        return Response({"error": "Can't find user"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def get(self, request, format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)
