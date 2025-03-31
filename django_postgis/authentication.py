from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .encryption import decrypt_token
from njoy_backend.models import User

class EncryptedTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        encrypted_token = request.COOKIES.get("token")
        if not encrypted_token:
            return None
        
        try:
            token = decrypt_token(encrypted_token)
        except Exception as e:
            raise AuthenticationFailed("Invalid or expired token.")
        
        try:
            user = User.objects.get(auth_token=token)
        except User.DoesNotExist:
            raise AuthenticationFailed("Invalid user associated with token.")
        
        return (user, token)