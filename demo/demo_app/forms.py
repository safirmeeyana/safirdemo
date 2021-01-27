from .models import shop
from django import forms

class ModeForm(forms.ModelForm):
    class Meta:
        model=shop
        fields=['name','desc','img','price']