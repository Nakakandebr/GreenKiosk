from django.urls import path
from .views import  vendor_upload_view
from .views import  vendors_list
from .views import  vendor_detail
from .views import  vendor_update_view
from .views import delete_vendor

urlpatterns  = [
    path('vendors/upload',vendor_upload_view, name='vendor_upload_view'),
    path("vendors/list", vendors_list , name="vendors_list"),
    path("vendor/<int:id>/", vendor_detail, name="vendor_detail"),
    path("vendor/edit/<int:id>/",  vendor_update_view, name="vendor_update_view"),
    path("vendor/delete/<int:id>/", delete_vendor , name="delete_vendor"),


]