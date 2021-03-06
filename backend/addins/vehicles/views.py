from rest_framework import viewsets, filters
from .serializers import VehicleSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vehicle

from backend.pagination import CustomPagination


# Create your views here.

class VehicleViewSet(viewsets.ModelViewSet):
    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    ordering_fields = ['id', 'vehicleregistrationnumber', 'make','model']
    search_fields = ('vehicleregistrationnumber', 'make','model', 'owner__first_name', 'owner__last_name')


@api_view(['GET'])
def get_vehicles(request):
    vehicles = Vehicle.objects.all()
    serializer_class = VehicleSerializer(vehicles, many = True)
    return Response(serializer_class.data)
