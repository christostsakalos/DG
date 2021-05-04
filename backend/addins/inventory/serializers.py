from rest_framework import serializers
from .models import Category, Part, Subcategory

    
class PartSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset= Subcategory.objects.all(), read_only=False)
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Part
        fields = ('id', 'name', 'description', 'quantity', 'category', 'category_name')


class SubcategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),read_only=False)
    parent_name = serializers.ReadOnlyField(source='parent.name')
    parts = PartSerializer(many=True, read_only=True)

    class Meta:
        model = Subcategory
        fields = ('id', 'name', 'parent', 'parent_name', 'parts')

class CategorySerializer(serializers.ModelSerializer): 
    sub_categories = SubcategorySerializer(many=True, read_only=True)
    
    
    class Meta:
        model = Category
        fields = ('id', 'name', 'sub_categories')

