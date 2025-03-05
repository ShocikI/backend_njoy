from cryptography.fernet import Fernet
from django.conf import settings

cipher = Fernet(settings.SECRET_KEY_AES)

def encrypt_token(token: str) -> str:
    return cipher.encrypt(token.encode()).decode()

def decrypt_token(encrypted_token: str) -> str:
    return cipher.decrypt(encrypted_token.encode()).decode()