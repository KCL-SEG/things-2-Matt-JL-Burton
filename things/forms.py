"""Forms of the project."""
from django import forms

from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea
        }

    # name = forms.CharField()
    # description = forms.CharField()
    # quantity = forms.IntegerField(min_value=0, max_value=50)