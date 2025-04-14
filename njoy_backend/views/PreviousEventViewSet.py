from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime

from njoy_backend.serializers import (
    EventSerializer, Event, 
)

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
    