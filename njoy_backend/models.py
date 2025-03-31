from django.db import models
from django.contrib.gis.db import models as geoModels
from django.contrib.auth.models import User as AuthUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class LinkType(models.Model):
    title = models.CharField(max_length=32, blank=False, unique=True)
    
    class Meta:
        verbose_name = ("Link type")
        verbose_name_plural = ("Link types")

    def __str__(self):
        return f"{self.title}"
    

class UserLink(models.Model):
    type = models.ForeignKey(LinkType, verbose_name=("Link type"), on_delete=models.CASCADE, blank=False)
    link_url = models.TextField(default="", blank=False)
    
    def __str__(self):
        return f"{self.type}"
    

class EventLink(models.Model):
    type = models.ForeignKey(LinkType, verbose_name=("Link type"), on_delete=models.CASCADE, blank=False)
    link_url = models.TextField(default="", blank=False)
    
    def __str__(self):
        return f"{self.type}"
    
    
class Categories(models.Model):
    title = models.CharField(max_length=32, blank=False, unique=True)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return f"{self.title}"
    

class User(AuthUser):
    description = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="images/avatars", blank=True)
    links = geoModels.ManyToManyField(UserLink, verbose_name=("Links"), blank=True)
    plus = models.IntegerField(default=0)
    minus = models.IntegerField(default=0)

    class Meta:
        verbose_name = ("User")
        verbose_name_plural = ("Users")

@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

        
class Event(geoModels.Model):
    title = geoModels.CharField(max_length=128, blank=False)
    owner = geoModels.ForeignKey(User, verbose_name=("Owner"), on_delete=geoModels.CASCADE, blank=False)
    date = geoModels.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    category = geoModels.ForeignKey(Categories, verbose_name=("Category"), on_delete=geoModels.CASCADE, blank=False)
    address = geoModels.CharField(max_length=255, blank=False)
    location = geoModels.PointField(geography=True, blank=False, null=False)
     
    links = geoModels.ManyToManyField(EventLink, verbose_name=("Links"), blank=True)
    image = geoModels.ImageField(upload_to="posters", height_field=None, width_field=None, max_length=None, blank=True)
    description = geoModels.TextField(max_length=2048, blank=True)
    price = geoModels.FloatField(default=0.0, blank=True)
    avaliable_places = geoModels.IntegerField(default=0, blank=True)
    init_date = geoModels.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = ("Event")
        verbose_name_plural = ("Events")

    def __str__(self):
        return f"{self.title}"