from rest_framework import viewsets

from njoy_backend.serializers import ( CategorySerializer,  Categories )

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Categories.objects.all()