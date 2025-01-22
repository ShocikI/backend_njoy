from django.contrib import admin

from models.Categories import Categories
from models.Event import Event
from models.User import User
from models.Link import EventLink, UserLink, LinkType

# Register your models here.
admin.site.register(Categories)
admin.site.register(Event)
admin.site.register(User)
admin.site.register(LinkType)
admin.site.register(UserLink)
admin.site.register(EventLink)