from rest_framework import serializers

from .models import Customer
from addins.vehicles.serializers import VehicleSerializer

# Thanks to drf documendation https://www.django-rest-framework.org/api-guide/relations/

class CustomerSerializer(serializers.ModelSerializer):
    owned_vehicles =  VehicleSerializer(many=True, read_only=True) 
    """ I'm setting read_only=True to update Customer without
    updating  owned_vehicles """
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
            "owned_vehicles",

        )
