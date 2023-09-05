from django.urls  import path
from .views import CustomerListView ,CustomerDetailView , VendorListView



urlpatterns=[
    path('customers/',CustomerListView.as_view() , name='customer_list_view'),
    path('customers/<int:id>/',CustomerDetailView.as_view() , name='customer_detail_view'),
    path('vendors/' , VendorListView.as_view() , name='vendor_detail_view'),
 
]   
