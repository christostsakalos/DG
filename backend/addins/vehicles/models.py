from django.db import models
from addins.customers.models import Customer

# Create your models here.
class Vehicle(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    vehicleregistrationnumber = models.CharField(max_length=255)
    fueltype = models.CharField(max_length=255, null=True)
    colour = models.CharField(max_length=255, null=True)
    owner = models.ForeignKey(to = Customer, on_delete=models.SET_NULL, related_name='owned_vehicles', null=True)
    
    
    def __str__(self):
        return '%s' % self.model