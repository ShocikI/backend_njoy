from django.contrib import admin

from njoy_backend.models import (Categories, Event, User, EventLink, UserLink, LinkType)

# Register your models here.
admin.site.register(Categories)
admin.site.register(Event)
admin.site.register(User)
admin.site.register(LinkType)
admin.site.register(UserLink)
admin.site.register(EventLink)