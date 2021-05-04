from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/', include('addins.customers.urls')),
    path('api/v1/', include('addins.vehicles.urls')),
    path('api/v1/', include('addins.inventory.urls')),
    path('api/v1/', include('addins.invoices.urls')),
    path('api/v1/', include('addins.jobsheets.urls'))
]
