from rest_framework import serializers

from .models import Jobsheet
from addins.vehicles.serializers import VehicleSerializer, Vehicle
from addins.customers.serializers import CustomerSerializer, Customer


class JobsheetSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(),read_only=False)
    make = serializers.ReadOnlyField(source='vehicle.make')
    model = serializers.ReadOnlyField(source='vehicle.model')
    vehicleregistrationnumber = serializers.ReadOnlyField(source='vehicle.vehicleregistrationnumber')
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), read_only=False)
    first_name = serializers.ReadOnlyField(source='customer.first_name')
    last_name = serializers.ReadOnlyField(source='customer.last_name')
    email = serializers.ReadOnlyField(source='customer.email')

    class Meta:
        model = Jobsheet
        fields = (
            "id",
            "reference_number",
            "customer",
            "first_name",
            "last_name",
            "email",
            "vehicle",
            "make",
            "model",
            "vehicleregistrationnumber",
            "notes",
            "datein",
            "datedue",
            "status",
            "paid",
            "remaining",

        )
