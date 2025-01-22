from django.db import models
from django.contrib.auth.models import User as AuthUser

class User(AuthUser):
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="images/avatars", blank=True)
    plus = models.IntegerField(default=0)
    minus = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")
