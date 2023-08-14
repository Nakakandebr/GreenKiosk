from django.urls import path
from .views import payment_create_view
# from .views import payment_detail

# from .views import payment_list
# from .views import payment_update_view
# from .views import payment_upload_view
# from .views import delete_payment

urlpatterns = [
    path('products/upload',payment_create_view, name="payment_create_view"),
    # path("products/list", payment_list , name="payment_list"),
    # path("product/<int:id>/", payment_detail, name="payment_detail"),
    # path("product/edit/<int:id>/", payment_update_view, name="payment_update_view"),
    # path("product/delete/<int:id>/", delete_payment , name="delete_payment"),
]