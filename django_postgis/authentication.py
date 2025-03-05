from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .encryption import decrypt_token

class EncryptedTokenAuthentication(TokenAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header:
            return None
        
        try:
            encrypted_token = auth_header.split(" ")[1]
            decrypt_token = decrypt_token(encrypted_token)
        except Exception:
            raise AuthenticationFailed
        
        return super().authenticate_credentials(decrypt_token)