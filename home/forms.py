from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    tel = forms.CharField(max_length=16)
    email = forms.EmailField()