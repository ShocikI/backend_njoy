from njoy_backend.models.Categories import Categories
from rest_framework import serializers

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'