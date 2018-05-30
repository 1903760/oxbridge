from django import forms
from .models import Order
from home.models import Test


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ["name", "phone", "level"]
