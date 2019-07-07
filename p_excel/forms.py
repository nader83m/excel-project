from django import forms
from django.core.validators import FileExtensionValidator


class UplodForm(forms.Form):
    file = forms.FileField(widget= forms.FileInput(attrs={'class' : 'form-control', 'placeholder': 'Example.xsl', 'id': 'efile', 'autofocus': 'autofocus'}))
