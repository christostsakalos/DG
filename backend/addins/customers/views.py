from rest_framework import viewsets

from .serializers import CustomerSerializer
from .models import Customer

from backend.pagination import CustomPagination


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = CustomPagination
    paginate_by = 10

    