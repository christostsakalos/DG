from django.contrib import admin
from .models import Category, Part, Subcategory
# Register your models here.

admin.site.register(Category)
admin.site.register(Part)
admin.site.register(Subcategory)
