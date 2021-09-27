from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer
from .models import Customer

from backend.pagination import CustomPagination


# Create your views here.

class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    ordering_fields = ['id', 'first_name', 'last_name','email']
    search_fields = ('first_name', 'last_name','email')


#https://www.django-rest-framework.org/tutorial/2-requests-and-responses/
@api_view(['GET'])
def get_owners(request):
    owners = Customer.objects.all()
    pagination_class = CustomPagination
    serializer_class = CustomerSerializer(owners, many = True)
    return Response(serializer_class.data)

    

    