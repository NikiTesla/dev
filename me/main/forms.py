from .models import Facts
from django.forms import ModelForm, TextInput, Textarea


class FactForms(ModelForm):
    class Meta:
        model = Facts
        fields = ["title", "fact"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
        }