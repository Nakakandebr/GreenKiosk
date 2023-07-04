from django.db import models


class Categories(models.Model):
    class Meta:
        verbose_name_plural = "categories"

    category_name = models.CharField(max_length=32)

    def all_categories():
        return Categories.objects.all()
    def __str__(self):
        return self.category_name