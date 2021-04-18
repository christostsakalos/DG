from rest_framework import serializers
from .models import Vehicle
from addins.customers.models import Customer



#Thanks to Django Rest documendation https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield
# and https://stackoverflow.com/questions/47265385/how-can-the-foreign-field-shows-the-name-instead-of-its-id
class VehicleSerializer(serializers.ModelSerializer): 
    owner = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(),read_only=False)
    first_name = serializers.ReadOnlyField(source='owner.first_name')
    last_name = serializers.ReadOnlyField(source='owner.last_name')
    
    class Meta:
        
        model = Vehicle
        fields = ('id', 'make', 'model', 'vehicleregistrationnumber', 'fueltype', 'colour', 'owner','first_name', 'last_name')