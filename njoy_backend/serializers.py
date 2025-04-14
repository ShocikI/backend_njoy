from rest_framework import serializers

from njoy_backend.models import User, Event, Categories, UserLink, EventLink, LinkType


class LinkTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkType
        fields = ("id", "title" )

class UserForEventSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ("username", "avatar")

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = ("id", "title")

class UserLinkSerializer(serializers.HyperlinkedModelSerializer):
    link_type = LinkTypeSerializer(many=False, required=True)
    class Meta:
        model = UserLink
        fields = ("link_type", "link_url")

class EventLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EventLink
        fields = ("type", "link_url")

class UserSerializer(serializers.HyperlinkedModelSerializer):
    links = UserLinkSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = (
            "username", "email", "date_joined", 
            "description", "avatar", "plus", "minus",
            "links"
        )

class EventSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserForEventSerializers(many=False, read_only=True, required=False)
    category = CategorySerializer(many=False, read_only=True, required=False)
    links = EventLinkSerializer(many=True, required=False)
    
    # Pola do zapisu (przyjmują id)
    owner_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=User.objects.all(),
        source='owner'
    )
    category_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Categories.objects.all(),
        source='category'
    )

    class Meta:
        model = Event
        fields = (
            "title", "date", "address", "location", "description", "price",
            "avaliable_places", "owner", "owner_id", "category", "category_id",
            "links", "image"
        )

    def create(self, validated_data):
        links = validated_data.pop("links", [])
        event = Event.objects.create(**validated_data)
        return event


class RegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {"password": { 'required': True, "write_only": True } }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
