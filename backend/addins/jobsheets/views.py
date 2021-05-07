from rest_framework import viewsets, filters
from django.db import connection
from rest_framework.decorators import api_view
from rest_framework.views import APIView
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
    'vehicle__first_name', 'vehicle__last_name')

@api_view(['GET'])
def paidchart(self):
    total_unpaid = 0
    total_paid = 0

    queryset = Jobsheet.objects.all()

    for entry in queryset:
        if entry.paid == False:
            total_unpaid += 1
        else:
            total_paid += 1

    data = [
        {
    'labels': ['Total Paid Jobs', 'Total Unpaid Jobs'],
    'datasets': [
        {
            'label': 'Jobs',
            'backgroundColor': ['rgb(54, 162, 235)', 'rgb(220,20,60)'],
            'data': [total_paid, total_unpaid]
        }
    ]
}

          
  
    ]

    
    return Response({'data':data})

@api_view(['Get'])
def completechart(self):
    total_complete = 0
    total_pending = 0

    queryset = Jobsheet.objects.all()

    for entry in queryset:
        if entry.status == 'Pending':
            total_pending += 1
        else:
            total_complete += 1
    data = [
        {
    'labels': ['Total Complete Jobs', 'Total Pending Jobs'],
    'datasets': [
        {
            'label': 'Jobs',
            'backgroundColor': ['rgb(54, 162, 235)', 'rgb(220,20,60)'],
            'data': [total_complete, total_pending]
        }
    ]
}

          
  
    ]
    return Response({'data':data})