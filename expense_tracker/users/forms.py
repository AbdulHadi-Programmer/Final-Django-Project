from django import forms
from .models import Expense

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['title', 'amount', 'category', 'date', 'description']
        widgets = {
            'description': forms.TextInput(attrs={'maxlength': 255}),  # Change from Textarea to TextInput
            'date': forms.DateInput(attrs={'type': 'date'}),  # Add a DateInput widget
        }

