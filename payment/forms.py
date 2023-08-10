from django import forms
from .models import Payment

class PymentUploadForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"

