from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Testimonial
from .forms import ContactForm
from django.urls import reverse


def index(request):
    testimonials = Testimonial.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formularz został pomyślnie wysłany!')
            return redirect(f"{reverse('index')}#contact")
        else:
            # Ustawienie wiadomości błędu tylko przy niepoprawnym formularzu
            messages.error(request, 'Wystąpił błąd w formularzu. Sprawdź dane i spróbuj ponownie.')
            return redirect(f"{reverse('index')}#contact")
    else:
        form = ContactForm()
    context = {
        'testimonials': testimonials,
        'form': form
    }
    return render(request, 'index.html', context)

def oferta(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formularz został pomyślnie wysłany!')
            return redirect(f"{reverse('oferta')}#contact")
        else:
            # Ustawienie wiadomości błędu tylko przy niepoprawnym formularzu
            messages.error(request, 'Wystąpił błąd w formularzu. Sprawdź dane i spróbuj ponownie.')
            return redirect(f"{reverse('oferta')}#contact")
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'oferta.html', context)

def portfolio(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, 'portfolio.html', context)

def omnie(request):
    testimonials = Testimonial.objects.all()
    context = {
        'testimonials': testimonials
    }
    return render(request, 'omnie.html', context)

def FAQ(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('oferta')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'FAQ.html', context)

def kontakt(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Formularz został pomyślnie wysłany!')
            return redirect(f"{reverse('kontakt')}#contact")
        else:
            # Ustawienie wiadomości błędu tylko przy niepoprawnym formularzu
            messages.error(request, 'Wystąpił błąd w formularzu. Sprawdź dane i spróbuj ponownie.')
            return redirect(f"{reverse('kontakt')}#contact")
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'kontakt.html', context)