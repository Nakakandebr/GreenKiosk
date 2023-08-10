from django import forms
from .models import Categories

class CategoriesUploadForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = "__all__"

