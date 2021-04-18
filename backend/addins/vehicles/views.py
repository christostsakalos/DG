from rest_framework import viewsets, filters
from .serializers import VehicleSerializer
from .models import Vehicle

from backend.pagination import CustomPagination


# Create your views here.

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('vehicleregistrationnumber', 'make','model', 'owner__first_name', 'owner__last_name')
