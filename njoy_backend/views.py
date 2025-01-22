from rest_framework import viewsets
from njoy_backend.serializers.UserSerializer import UserSerializer, User
from njoy_backend.serializers.EventSerializer import EventSerializer, Event
from njoy_backend.serializers.CategorySerializer import CategorySerializer, Categories
from njoy_backend.serializers.LinkSerializer import (
    LinkType, UserLink, EventLink, LinkTypeSerializer, UserLinkSerializer, EventLinkSerializer, 
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
class LinkTypeViewSet(viewsets.ModelViewSet):
    queryset = LinkType.objects.all()
    serializer_class = LinkTypeSerializer

class EventLinkViewSet(viewsets.ModelViewSet):
    queryset = EventLink.objects.all()
    serializer_class = EventLinkSerializer

class UserLinkViewSet(viewsets.ModelViewSet):
    queryset = UserLink.objects.all()
    serializer_class = UserLinkSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer