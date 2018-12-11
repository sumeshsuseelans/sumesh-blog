from django import forms
from .models import Items

class ItemsForm(forms.ModelForm):
	class Meta:
		model = Items
		fields= ["item","Description","ItemImage"]

class ContactForm(forms.Form):
    fullname = forms.CharField()
    email = forms.CharField()
    contact = forms.CharField()