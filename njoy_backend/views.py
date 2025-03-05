from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D
from datetime import datetime


from njoy_backend.serializers import (
    RegistrationSerializer, User, 
    EventSerializer, Event, 
    CategorySerializer, Categories,
    LinkTypeSerializer, LinkType, 
    UserLinkSerializer, UserLink, 
    EventLinkSerializer, EventLink, 
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = RegistrationSerializer
    queryset = User.objects.all()


class UpcommingEventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def list(self, request, *args, **kwargs):
        today = datetime.now()
        point = self.request.query_params.getlist('point')
        radius = self.request.query_params.getlist('radius')
        categoryIds = self.request.query_params.getlist('categoryIds')

        if point and radius:
            # Prepare point data
            lon, lat = str(*point).split("-")
            lon = float(lon)
            lat = float(lat)
            current_point = Point(lon, lat, srid=4326)
            current_radius = float(radius[0])

            # Get the not expired events
            queryset = Event.objects.filter(date__gt=today)
            # Get events in radius from user position
            queryset = queryset.filter(
                location__distance_lte=(current_point, D(km=current_radius))
                ).annotate(
                    distance=Distance('location', current_point)
            )
            # Get event according to category
            if categoryIds != ['']:
                queryset = queryset.filter(category__in=categoryIds)

            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class PreviousEventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def list(self, request, *args, **kwargs):
        today = datetime.now()
        queryset = Event.objects.filter(date__lt=today)

        categoryIds = self.request.query_params.getlist('category')
        if categoryIds != ['']:
            queryset = queryset.filter(category__in=categoryIds)

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