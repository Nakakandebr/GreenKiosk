from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=32)

    def all_categories():
        return Categories.objects.all()
    def __str__(self):
        return self.category_name