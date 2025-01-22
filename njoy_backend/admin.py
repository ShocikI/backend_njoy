from django.contrib import admin

from njoy_backend.models.Categories import Categories
from njoy_backend.models.Event import Event
from njoy_backend.models.User import User
from njoy_backend.models.Link import EventLink, UserLink, LinkType

# Register your models here.
admin.site.register(Categories)
admin.site.register(Event)
admin.site.register(User)
admin.site.register(LinkType)
admin.site.register(UserLink)
admin.site.register(EventLink)