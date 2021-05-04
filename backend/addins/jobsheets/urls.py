from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import JobsheetViewSet

router = DefaultRouter()
router.register("jobsheets", JobsheetViewSet, basename="jobsheets")

urlpatterns = [
    path('', include(router.urls)),
]
