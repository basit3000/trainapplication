from django import forms
from .models import Locations

class LocationForm(forms.ModelForm):
    class Meta:
        model = Locations
        fields = ['name', 'text', 'city', 'state', 'zip_code']