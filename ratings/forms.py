from django import forms
from .models import Reviews_and_Ratings

class RatingUploadForm(forms.ModelForm):
    class Meta:
        model = Reviews_and_Ratings
        fields = "__all__"

