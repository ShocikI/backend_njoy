from rest_framework import viewsets

from njoy_backend.serializers import ( LinkTypeSerializer, LinkType )

    
class LinkTypeViewSet(viewsets.ModelViewSet):
    serializer_class = LinkTypeSerializer
    queryset = LinkType.objects.all()