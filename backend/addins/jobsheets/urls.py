from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import JobsheetViewSet, paidchart, completechart
router = DefaultRouter()
router.register("jobsheets", JobsheetViewSet, basename="jobsheets")

urlpatterns = [
    path('', include(router.urls)),
    path('paidchart', paidchart, name='paidchart'),
    path('completechart', completechart, name='completechart')
]
