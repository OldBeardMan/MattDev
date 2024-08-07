from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'company', 'message']  # Dodane pole company
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź swoje imię...'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+48 123 456 789'}),
            'company': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Wprowadź nazwę firmy...'}),  # Widget dla pola company
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Wprowadź swoją wiadomość...', 'style': 'height: 10rem'}),
        }
        labels = {
            'name': 'Imię:',
            'email': 'E-mail:',
            'phone': 'Numer telefonu:',
            'company': 'Firma:',  # Etykieta dla pola company
            'message': 'Wiadomość:',
        }
