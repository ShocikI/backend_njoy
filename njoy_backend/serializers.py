from rest_framework import serializers

from njoy_backend.models import User, Event, Categories, UserLink, EventLink, LinkType


class LinkTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkType
        fields = '__all__'

class UserForEventSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "avatar")

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ('title',)

class UserLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserLink
        fields = ('type', 'link_url')

class EventLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLink
        fields = ('type', 'link_url')

class EventSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserForEventSerializers(many=False)
    category = CategorySerializer(many=False)
    links = EventLinkSerializer(many=True)

    class Meta:
        model = Event
        fields = ("title", "date", "address", "location", "description", "price", "avaliable_places", "owner", "category", "links", "image")

class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {"password": { 'required': True, "write_only": True } }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
