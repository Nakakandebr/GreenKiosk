from django.urls import path
from .views import customer_upload_view
from .views import  customer_list
from .views import customer_detail
from .views import customer_update_view
from .views import delete_customer
from django.conf import settings
from django.conf.urls.static  import static

urlpatterns = [
    path('customer/upload',customer_upload_view, name='customer_upload_view'),
    path("customer/list", customer_list , name="customer_list"),
    path("customer/<int:id>/",customer_detail, name="customer_detail"),
    path("customer/edit/<int:id>/",customer_update_view, name="customer_update_view"),
    path("customer/delete/<int:id>/", delete_customer , name="delete_customer"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)