from django.urls import path
from .views import product_get_view

urlpatterns = [
    path('products/get',product_get_view, name='product_get_view'),
]