from rest_framework import serializers
from customer.models import Customer
from vendors.models import Vendor

class CustomerSerializer(serializers.ModelSerializer):
    # serialises and deserialises
    class Meta:
        model = Customer
        fields = '__all__'


# Define a serializer class for the Vendor model.
class VendorSerializer(serializers.ModelSerializer):

    # Meta class to provide metadata for the serializer.
    class Meta:
        
        # Specify the model that this serializer will be used for (Vendor model).
        model = Vendor
        
        # Include all fields from the Vendor model in the serialization.
        fields = '__all__'
