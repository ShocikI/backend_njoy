from django.db import models
from User import User
from Event import Event

class LinkType(models.Model):
    title = models.CharField(max_length=32, blank=False, unique=True)
    
    class Meta:
        verbose_name = ("Link type")
        verbose_name_plural = ("Link types")

    def __str__(self):
        return f"{self.title}"
    
    
class UserLink(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.CASCADE, blank=False)
    type = models.ForeignKey(LinkType, verbose_name=("Link type"), on_delete=models.CASCADE, blank=False)
    link_url = models.TextField(default="", blank=False)
    
    def __str__(self):
        return f"{self.user} {self.type}"
    

class EventLink(models.Model):
    event = models.ForeignKey(Event, verbose_name=("Event"), on_delete=models.CASCADE, blank=False)
    type = models.ForeignKey(LinkType, verbose_name=("Link type"), on_delete=models.CASCADE, blank=False)
    link_url = models.TextField(default="", blank=False)
    
    def __str__(self):
        return f"{self.event.title} {self.type}"
    