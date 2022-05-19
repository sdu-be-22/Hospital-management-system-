from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['customer', 'date_ordered', 'complete', ' transaction_id']
