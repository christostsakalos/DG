from rest_framework import viewsets, filters
from .serializers import CategorySerializer, SubcategorySerializer, PartSerializer
from .models import Category, Part, Subcategory
from backend.pagination import CategoryPagination, CustomPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    pagination_class = CategoryPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')




class SubcategoryViewSet(viewsets.ModelViewSet):
    serializer_class = SubcategorySerializer
    queryset = Subcategory.objects.all()
    pagination_class = CategoryPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name')


@api_view(['GET'])
def get_parents(request):
    parents = Category.objects.all()
    serializer_class = CategorySerializer(parents, many = True)
    return Response(serializer_class.data)

class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    pagination_class = CustomPagination
    filter_backends = (filters.SearchFilter,)
    # https://stackoverflow.com/questions/35129820/properly-using-foreign-key-references-in-search-fields-django-admin
    # To search on a foreign key, we use __
    search_fields = ('name', 'quantity', 'description', 'category__name')

@api_view(['GET'])
def get_categories(request):
    categories = Subcategory.objects.all()
    serializer_class = SubcategorySerializer(categories, many = True)
    return Response(serializer_class.data)