from django.contrib import admin
from .models import Customer



# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "password", "email","phonenumber" , "address" )
admin.site.register(Customer,CustomerAdmin )
