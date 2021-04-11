from rest_framework import serializers

from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Customer
        read_only_fields = (
            "created_at",
        ),
        fields = (
            "id",
            "reference_number",
            "first_name",
            "last_name",
            "email",
            "org_name",
            "address",
            "city",
            "country",
            "postcode",
            "country",
        )