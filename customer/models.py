from django.db import models

# Create your models here.
class Customer(models.Model):
    firstname=models.CharField(max_length=42)
    lastname=models.CharField(max_length=42)
    email=models.EmailField(max_length=200)
    phonenumber=models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    address=models.CharField(max_length=32)
    
    def register(self):
        self.save
        def get_customer_by_email(email):
            try:
                return Customer.objects.get(email=email)
            except:
                return False
        def isExist(self):
                if Customer.objects.filter(email = self.email):
                    return True
                return False
    

