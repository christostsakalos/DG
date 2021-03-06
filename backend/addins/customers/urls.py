from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import CustomerViewSet, get_owners

router = DefaultRouter()
router.register("customers", CustomerViewSet, basename="customers")


urlpatterns = [
    path('', include(router.urls)),
    path('getowners', get_owners),
]
