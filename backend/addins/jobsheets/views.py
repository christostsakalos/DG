from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import JobsheetSerializer
from .models import Jobsheet

from backend.pagination import CustomPagination


# Create your views here.

class JobsheetViewSet(viewsets.ModelViewSet):
    serializer_class = JobsheetSerializer
    queryset = Jobsheet.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('reference_number', 'vehicle__make','vehicle__model', 'vehicle__vehicleregistrationnumber', 
    'customer__first_name', 'customer__last_name')