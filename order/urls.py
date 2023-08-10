from django.urls import path
from .views import order_upload_view
from .views import orders_list
from .views import order_detail
from .views import order_update_view
from .views import delete_order

urlpatterns = [
    path('orders/upload',order_upload_view, name='order_upload_view'),
    path("orders/list", orders_list , name="orders_list"),
    path("order/<int:id>/", order_detail, name="order_detail"),
    path("order/edit/<int:id>/", order_update_view, name="order_update_view"),
    path("order/delete/<int:id>/", delete_order, name="delete_order"),
]