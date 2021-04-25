from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, SubcategoryViewSet, PartViewSet, get_parents, get_categories

router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("subcategories", SubcategoryViewSet, basename="subcategories")
router.register('parts',PartViewSet, basename="parts")

urlpatterns = [
    path('', include(router.urls)),
    path('getparents', get_parents),
    path('getcategories', get_categories),
]
