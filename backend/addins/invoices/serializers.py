from rest_framework import serializers

from .models import Invoice, Item
from addins.customers.models import Customer

class ItemSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Item
        read_only_fields = (
            "invoice",
        )
        fields = (
            "id",
            "title",
            "quantity",
            "unit_price",
            "net_amount",
            "vat_rate",
            "discount"
        )

class InvoiceSerializer(serializers.ModelSerializer):   
    items = ItemSerializer(many=True)
    bankaccount = serializers.CharField(required=False)
    first_name = serializers.ReadOnlyField(source='customer.first_name')
    last_name = serializers.ReadOnlyField(source='customer.last_name')
    email = serializers.ReadOnlyField(source='customer.email')
    address = serializers.ReadOnlyField(source='customer.address')
    city = serializers.ReadOnlyField(source='customer.city')
    postcode = serializers.ReadOnlyField(source='customer.postcode')

    class Meta:
        model = Invoice
        read_only_fields = (
            "team",
            "created_at",
            "created_by",
            "modified_at",
            "modified_by",
        ),
        fields = (
            "id",
            "customer",
            "first_name",
            "last_name",
            "email",
            "address",
            "city",
            "postcode",
            "due_days",
            "get_due_date_formatted",
            "bankaccount",
            "is_sent",
            "is_paid",
            "gross_amount",
            "vat_amount",
            "net_amount",
            "discount_amount",
            "items",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        invoice = Invoice.objects.create(**validated_data)

        for item in items_data:
            Item.objects.create(invoice=invoice, **item)
        
        return invoice