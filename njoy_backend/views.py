from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime

from njoy_backend.serializers import (
    UserSerializer, User, 
    EventSerializer, Event, 
    CategorySerializer, Categories,
    LinkTypeSerializer, LinkType, 
    UserLinkSerializer, UserLink, 
    EventLinkSerializer, EventLink, 
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UpcommingEventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        today = datetime.now()
        categoryIds = self.request.query_params.getlist('category')
        if categoryIds:
            queryset = Event.objects.filter(date__gt=today).filter(category__in=categoryIds)
        else:
            queryset = Event.objects.filter(date__gt=today)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class ArchiveEventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def list(self, request, *args, **kwargs):
        today = datetime.now()
        categoryIds = self.request.query_params.getlist('category')
        if categoryIds:
            queryset = Event.objects.filter(date__lt=today).filter(category__in=categoryIds)
        else:
            queryset = Event.objects.filter(date__lt=today)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
class LinkTypeViewSet(viewsets.ModelViewSet):
    serializer_class = LinkTypeSerializer
    queryset = LinkType.objects.all()

class EventLinkViewSet(viewsets.ModelViewSet):
    serializer_class = EventLinkSerializer
    queryset = EventLink.objects.all()

class UserLinkViewSet(viewsets.ModelViewSet):
    serializer_class = UserLinkSerializer
    queryset = UserLink.objects.all()

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()