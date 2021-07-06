from django.db.models import fields
from .models import mymodel
from django import forms

class CreateNewUrl(forms.ModelForm):
    class Meta:
        model = mymodel
        fields = {'old_url'}
        widgets = {
            'old_url':forms.TextInput(attrs={'class':'form-control'})
        }