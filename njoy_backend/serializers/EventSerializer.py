from njoy_backend.models.Event import Event
from rest_framework import serializers

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

        