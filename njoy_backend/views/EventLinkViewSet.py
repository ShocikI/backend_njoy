from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from django_postgis.authentication import EncryptedTokenAuthentication
from njoy_backend.permissions import IsOwnerOrReadOnly
from njoy_backend.serializers import ( EventLinkSerializer )
from njoy_backend.models import ( User, Event, EventLink )

class EventLinkViewSet(viewsets.ModelViewSet):
    serializer_class = EventLinkSerializer
    authentication_classes = [ EncryptedTokenAuthentication ]
    permission_classes = [ IsOwnerOrReadOnly ]
    queryset = EventLink.objects.all()

    def get_queryset(self):
        pk = self.kwargs.get('event_pk')
        if pk:
            user = get_object_or_404(Event, pk=pk)
            return EventLink.objects.filter(owner=user)
        return EventLink.objects.none()

    def perform_create(self, serializer):
        username = self.kwargs.get("username_username")
        user = get_object_or_404(User, username=username)
        serializer.save(owner=user)