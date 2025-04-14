from rest_framework import viewsets

from njoy_backend.serializers import ( EventLinkSerializer, EventLink )


class EventLinkViewSet(viewsets.ModelViewSet):
    serializer_class = EventLinkSerializer
    queryset = EventLink.objects.all()
