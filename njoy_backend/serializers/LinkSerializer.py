from njoy_backend.models.Link import UserLink, EventLink, LinkType
from rest_framework import serializers

class LinkTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkType
        fields = '__all__'

class UserLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLink
        fields = '__all__'

class EventLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLink
        fields = '__all__'