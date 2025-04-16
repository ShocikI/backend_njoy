from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from datetime import datetime

from njoy_backend.models import Event, User
from njoy_backend.serializers import EventSerializer
from django_postgis.authentication import EncryptedTokenAuthentication

class UserEventsViewSet(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = [EncryptedTokenAuthentication]
    
    def get(self, request, username):
        today = datetime.now()
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user_events = Event.objects.filter(owner=user)
        past_events = user_events.filter(date__lt=today)
        upcoming_events = user_events.filter(date__gt=today)

        past_events_serializer = EventSerializer(past_events, many=True)
        upcoming_events_serializer = EventSerializer(upcoming_events, many=True)

        return Response(
            {
                "past_events": past_events_serializer.data,
                "upcoming_events": upcoming_events_serializer.data
            }, 
            status=status.HTTP_200_OK
        )