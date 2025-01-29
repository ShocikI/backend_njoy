from rest_framework import serializers

from njoy_backend.models import User, Event, Categories, UserLink, EventLink, LinkType


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserForEventSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "avatar")

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('title',)

class EventSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserForEventSerializers(many=False)
    category = CategorySerializer(many=False)
    
    class Meta:
        model = Event
        fields = ("title", "date", "address", "location", "description", "price", "avaliable_places", "owner", "category", "image")


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