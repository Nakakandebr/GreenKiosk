from django.urls import path
from .views import cart_upload_view
from .views import cart_list
from .views import cart_detail
from .views import cart_update_view
from .views import delete_cart

urlpatterns = [
    path('cart/upload',cart_upload_view, name='cart_upload_view'),
    path("cart/list", cart_list , name="cart_list"),
    path("cart/<int:id>/", cart_detail, name="cart_detail"),
    path("cart/edit/<int:id>/", cart_update_view, name="cart_update_view"),
    path("cart/delete/<int:id>/", delete_cart , name="delete_cart"),
]