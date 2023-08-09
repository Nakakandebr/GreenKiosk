from django.contrib import admin
from .models import Vendor
# Register your models here.
class VendorAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone","image")
admin.site.register(Vendor, VendorAdmin)