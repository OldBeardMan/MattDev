from django.shortcuts import render, redirect
from .models import Testimonial
from .forms import ContactForm


def index(request):
    testimonials = Testimonial.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
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
            return redirect('oferta')
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
    return render(request, 'omnie.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def kontakt(request):
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
    return render(request, 'kontakt.html', context)