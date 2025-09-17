from django import forms
from .models import Entry
from .models import Category

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['entry_type', 'value', 'date', 'category', 'comment']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'comment': forms.Textarea(attrs={'rows': 2}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'New category name'})
        }
