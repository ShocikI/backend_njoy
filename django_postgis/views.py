from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .encryption import encrypt_token
from .authentication import EncryptedTokenAuthentication

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if user: 
            token, _ = Token.objects.get_or_create(user=user)
            encrypted_token = encrypt_token(token.key)

            response = Response({"message": "Logged in"}, status=status.HTTP_200_OK)
            response.set_cookie(
                key="token", value=encrypted_token,
                httponly=True, 
                secure=True,
                samesite="None",
                max_age=86400,
            )
            return response

        return Response({"error": "Invalid crenetials"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes = [EncryptedTokenAuthentication]
    permission_classes = [AllowAny]

    def post(self, request):
        response = Response({"message": "Logged out"}, status=status.HTTP_200_OK)
        response.delete_cookie(
            "token",
            samesite="None",
            path='/'
        )

        return response

class CheckLoginView(APIView):
    authentication_classes = [EncryptedTokenAuthentication]
    permission_classes = [AllowAny]

    def get(self, request, format=None):
        if request.user.is_authenticated:
            return Response({
                "user": request.user.username, 
            }, status=status.HTTP_200_OK)
        
        return Response({
            "user": None,
        }, status=status.HTTP_200_OK)
