from django.contrib import admin
from .models import Payment

# Register your models here.
# class PaymentAdmin(admin.ModelAdmin):
    # list_display = ("amount","currency","date","method","customer_id","order_id")
# admin.site.register(Payment,PaymentAdmin)

admin.site.register(Payment)






