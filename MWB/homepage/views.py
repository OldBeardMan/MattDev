from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def oferta(request):
    return render(request, 'oferta.html')

def portfolio(request):
    return render(request, 'portfolio.html')

def omnie(request):
    return render(request, 'omnie.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def kontakt(request):
    return render(request, 'kontakt.html')