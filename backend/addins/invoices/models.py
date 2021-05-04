from django.db import models
import decimal
from datetime import timedelta
from django.contrib.auth.models import User
from addins.customers.models import Customer

# Create your models here.

class Invoice(models.Model):
    due_days = models.IntegerField(default=14)
    is_credited = models.BooleanField(default=False)
    is_sent = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    bankaccount = models.CharField(max_length=266, null=True)
    gross_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat_amount = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    discount_amount = models.DecimalField(max_digits=6, decimal_places=2)
    customer = models.ForeignKey(Customer, related_name='invoices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.id

    class Meta:
        ordering = ('-created_at',)
    
    def get_due_date(self):
        return self.created_at + timedelta(days=self.due_days)
    
    def get_due_date_formatted(self):
        return self.get_due_date().strftime("%d.%m.%Y")

class Item(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    net_amount = models.DecimalField(max_digits=6, decimal_places=2)
    vat_rate = models.IntegerField(default=0)
    discount = models.IntegerField(default=0)

    def get_gross_amount(self):
        vat_rate = decimal.Decimal(self.vat_rate/100)
        return self.net_amount + (self.net_amount * vat_rate)