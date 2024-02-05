from django import forms
from . models import Inventory

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['name', 'lot_number', 'expiration_date']
        labels = {'name': 'Name', 'lot_number': 'Lot Number', 'expiration_date': 'Expiration Date'}
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'lot_number': forms.TextInput(attrs={'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'class': 'form-control'}),
        }