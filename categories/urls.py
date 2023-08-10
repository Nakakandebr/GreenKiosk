from django.urls import path
from .views import categories_upload_view
from .views import categories_list
from .views import category_detail
from .views import category_update_view
from .views import delete_category

urlpatterns = [
    path('categories/upload',categories_upload_view, name='category_upload_view'),
    path("categories/list", categories_list, name="categories_list"),
    path("product/<int:id>/",category_detail, name="categories_detail"),
    path("product/edit/<int:id>/", category_update_view, name="category_update_view"),
    path("product/delete/<int:id>/", delete_category , name="delete_category"),
]