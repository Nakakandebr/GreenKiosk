from django.urls import path
from .views import cart_upload
from .views import list_cart
from .views import cart_detail
from .views import delete_cart
from .views import cart_edit



urlpatterns = [

    path("cart/<int:id>/",cart_detail, name="cart_detail"),
    path("product/delete/<int:id>/", delete_cart , name="delete_cart"),
    path('cart/edit/<int:id>/', cart_edit, name='edit_cart'),
    path('cart/upload/', cart_upload, name='cart_view'),
    path('cart/list/', list_cart, name='list_cart'),
   
        ]