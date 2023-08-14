
from django.core.exceptions import ValidationError
from django.db import models

class Payment(models.Model):
    AMOUNT_CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('UGX', 'Ugx'),
        ('KES', 'Kenyan Shilling'),
        # Add more currency choices as needed
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('mobile_money', 'Mobile Money'),
        # Add more payment method choices as needed
    ]
    
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3, choices=AMOUNT_CURRENCY_CHOICES)
    date = models.DateTimeField(auto_now=True)
    method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()
    card_number = models.CharField(max_length=16, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    cvv = models.CharField(max_length=4, blank=True, null=True)
    paypal_email = models.EmailField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.method == 'credit_card':
            if not all([self.card_number, self.expiration_date, self.cvv]):
                raise ValidationError("Credit card information is incomplete")
        elif self.method == 'paypal':
            if not self.paypal_email:
                raise ValidationError("PayPal email is required")
        elif self.method == 'mobile_money':
           
            pass
        else:
            raise ValidationError("Invalid payment method")

        super().save(*args, **kwargs)
