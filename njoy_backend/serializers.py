from rest_framework import serializers

from njoy_backend.models.User import User
from njoy_backend.models.Event import Event
from njoy_backend.models.Categories import Categories
from njoy_backend.models.Link import UserLink, EventLink, LinkType


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        # fields = ("title", "date", "address", "location", "description", "price", "avaliable_places", "owner", "category", "image")
        fields = '__all__'

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

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