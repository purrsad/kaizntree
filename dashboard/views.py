from rest_framework import viewsets
from .models import Items
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Items.objects.all()
    serializer_class = ItemSerializer
