from rest_framework.views import APIView
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from django_postgis.authentication import EncryptedTokenAuthentication
from njoy_backend.serializers import ( EventLinkSerializer )
from njoy_backend.models import (EventLink, Event)


class EventLinksByIdView(APIView):
    authentication_classes = [EncryptedTokenAuthentication]
    permission_classes = [permissions.AllowAny]

    def get(self, request, pk=None):
        try:
            user = Event.objects.get(pk=pk)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = EventLink.objects.filter(owner=user)
        serializer = EventLinkSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
