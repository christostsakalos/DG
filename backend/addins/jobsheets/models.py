from django.db import models
from datetime import timedelta
from addins.customers.models import Customer
from addins.vehicles.models import Vehicle

# Create your models here.

class Jobsheet(models.Model):
    reference_number = models.IntegerField(null=True)
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
        return '%s' % self.vehicle

    class Meta:
        ordering = ('-datein',)

    def get_paid_format(self):
        is_paid = 'job_paid'
        is_unpaid = 'job_unpaid'
        if self.paid == True:
            return is_paid
        else:
            return is_unpaid

