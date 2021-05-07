from rest_framework import serializers

from .models import Jobsheet
from addins.vehicles.serializers import VehicleSerializer, Vehicle


class JobsheetSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all(),read_only=False)
    make = serializers.ReadOnlyField(source='vehicle.make')
    model = serializers.ReadOnlyField(source='vehicle.model')
    vehicleregistrationnumber = serializers.ReadOnlyField(source='vehicle.vehicleregistrationnumber')
    first_name = serializers.ReadOnlyField(source='vehicle.owner.first_name')
    last_name = serializers.ReadOnlyField(source='vehicle.owner.last_name')
    email= serializers.ReadOnlyField(source='vehicle.owner.email')

    class Meta:
        model = Jobsheet
        fields = (
            "id",
            "reference_number",
            "first_name",
            "last_name",
            "vehicle",
            "make",
            "email",
            "model",
            "vehicleregistrationnumber",
            "get_paid_format",
            "notes",
            "datein",
            "datedue",
            "status",
            "paid",
            "remaining",

        )
