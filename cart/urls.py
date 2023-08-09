from django.urls import path
from .views import product_get_view
from .views import cart_list

urlpatterns = [
    path('products/get',product_get_view, name='product_get_view'),
    path("products/list",cart_list, name="cart_list"),
]