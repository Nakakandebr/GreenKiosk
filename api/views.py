from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # Import status to handle HTTP status codes
from customer.models import Customer
from .serializers import CustomerSerializer

from vendors.models import Vendor
from .serializers import VendorSerializer

class CustomerListView(APIView):

    def get(self, request):
        # Retrieve all customers from the database
        customers = Customer.objects.all()

        # Serialize the queryset using CustomerSerializer
        serializer = CustomerSerializer(customers, many=True)

        # Return the serialized data in the response
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self, request):
    # Create a new instance of the CustomerSerializer and populate it with the data from the incoming HTTP request.
       serializer = CustomerSerializer(data=request.data)

    # Check if the data provided in the request is valid according to the serializer's rules.
       if serializer.is_valid():
        # If the data is valid, save the serialized data to create a new Customer record in the database.
        serializer.save()
        
        # Return a success response with the serialized data and an HTTP status code of 201 (Created).
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    # If the data is not valid, return a response containing the validation errors and an HTTP status code of 400 (Bad Request).
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerDetailView(APIView):
#     def get(self, request , id , format=None):
#         customer = Customer.objects.get(id=id)
#         serializer = CustomerSerializer(customer)
#         return Response(serializer.data)
   
    def get(self, request, id, format=None):
        # Retrieve a Customer object from the database with the specified 'id'.
        customer = Customer.objects.get(id=id)
        
        # Serialize the retrieved Customer object using the CustomerSerializer.
        serializer = CustomerSerializer(customer)
        
        # Return a response containing the serialized customer data.
        return Response(serializer.data)


    def put(self, request, id, format=None):
           customer = Customer.objects.get(id=id)
           serializer = CustomerSerializer(customer, data=request.data)  # Change 'request.data' here
           if serializer.is_valid():
               serializer.save()
               return Response(serializer.data, status=status.HTTP_200_OK)  # Fix 'status.HTPP_200_OK' to 'status.HTTP_200_OK'
           return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    
    
    def delete(self , request , id, format=None):
        customer = Customer.objects.get(id=id)
        customer.delete()
        return Response("Customer deleted" , status=status.HTTP_204_NO_CONTENT)
    



class VendorListView(APIView):
    def get(self , request):
        vendors = Vendor.objects.all()
        serializer  = VendorSerializer(vendors , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.error , status=status.HTTP_400_BAD_REQUEST)
    


    



