from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from django_postgis.authentication import EncryptedTokenAuthentication
from njoy_backend.permissions import IsEventOwnerOrReadOnly
from njoy_backend.serializers import ( EventLinkSerializer )
from njoy_backend.models import ( User, Event, EventLink )

class EventLinkViewSet(viewsets.ModelViewSet):
    serializer_class = EventLinkSerializer
    authentication_classes = [ EncryptedTokenAuthentication ]
    permission_classes = [ IsEventOwnerOrReadOnly ]
    queryset = EventLink.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('event_pk')
        if pk:
            event = get_object_or_404(Event, pk=pk)
            return EventLink.objects.filter(owner=event)
        return EventLink.objects.none()

    def perform_create(self, serializer):
        event_pk = self.kwargs.get("event_pk")
        event = get_object_or_404(Event, pk=event_pk)
        serializer.save(owner=event)