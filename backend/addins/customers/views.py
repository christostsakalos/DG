from rest_framework import viewsets, filters

from .serializers import CustomerSerializer
from .models import Customer

from backend.pagination import CustomPagination


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'last_name','email')

    

    