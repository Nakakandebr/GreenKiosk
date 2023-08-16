from django.contrib import admin
from .models import Categories

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name"]
admin.site.register(Categories,CategoryAdmin)