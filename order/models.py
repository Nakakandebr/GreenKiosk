from django.db import models
from cart.models import Product_Cart
from customer.models import Customer
from delivery.models import Delivery

class Order(models.Model):
    basket = models.ForeignKey(Product_Cart, null=True, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,null=True, on_delete=models.CASCADE )
    delivery = models.OneToOneField(Delivery,null=True, on_delete=models.CASCADE )
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)