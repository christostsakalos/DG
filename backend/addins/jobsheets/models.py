from django.db import models
from datetime import timedelta
from addins.customers.models import Customer
from addins.vehicles.models import Vehicle

# Create your models here.

class Jobsheet(models.Model):
    reference_number = models.IntegerField(null=True)
    customer = models.ForeignKey(to = Customer, on_delete=models.SET_NULL, related_name='jobs', null=True)
    vehicle = models.ForeignKey(to = Vehicle, on_delete=models.SET_NULL, related_name='jobs', null=True)
    notes = models.CharField(max_length=255, null=True)
    datein = models.DateField( auto_now_add=True)
    datedue = models.DateField(null=True,)
    STATUSES = ( 
        ('Complete', 'Complete'),
        ('Pending', 'Pending'),
        )
    status = models.CharField(max_length=10, choices=STATUSES, default='P')
    paid = models.BooleanField(default=False)
    remaining = models.IntegerField(null=True)

    def __str__(self):
        return '%s' % self.customer

    class Meta:
        ordering = ('-datein',)
