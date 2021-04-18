from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import VehicleViewSet

router = DefaultRouter()
router.register("vehicles", VehicleViewSet, basename="vehicles")

urlpatterns = [
    path('', include(router.urls)),
]
