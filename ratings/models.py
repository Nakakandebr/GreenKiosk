from django.db import models

# Create your models here.
class Reviews_and_Ratings(models.Model):
    class Meta:
        verbose_name_plural = "reviews_and_ratings"
        
    title = models.CharField(max_length=32)
    review_Content = models.CharField(max_length=32)
    rating = models.IntegerField()
    cumulative_ratings=models.IntegerField()
    author=models.CharField(max_length=32)
    created_date = models.DateTimeField()