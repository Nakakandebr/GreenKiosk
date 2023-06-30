from django.db import models

# Create your models here.

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    date = models.DateTimeField(auto_now =True)
    method = models.CharField(max_length=10)
    customer_id = models.IntegerField()
    order_id = models.IntegerField()

    def is_valid(self):
        # Check if the amount is positive
        if self.amount <= 0:
            return False

        # Check if the currency is valid
        if self.currency not in ["KES", "UG", "TZ"]:
            return False

        # Check if the date is in the future
        if datetime.date.today() > self.date:
            return False

        # Check if the method is valid
        if self.method not in ["M-Pesa", "Cash", "PayPal"]:
            return False

        # Check if the customer ID is valid
        if not customer_id:
            return False

        # Check if the order ID is valid
        if not order_id:
            return False

        return True

    def fulfill(self):
        # Check if the payment is valid
        if not self.is_valid():
            return False

        
 
        return True
