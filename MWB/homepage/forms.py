from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź swoje imię...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+48 123 456 789'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Wprowadź swoją wiadomość...', 'style': 'height: 10rem'}),
        }
        labels = {
            'name': 'Pełne imię',
            'email': 'Adres e-mail',
            'phone': 'Numer telefonu',
            'message': 'Wiadomość',
        }
