from django.db import models

# Create your models here.
class Delivery(models.Model):
    class Meta:
        verbose_name_plural = "delivery"
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phoneNumber = models.CharField(max_length=20)
    delivery_time = models.DateTimeField()
    is_delivered = models.BooleanField(default=False)


