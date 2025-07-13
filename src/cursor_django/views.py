from django.shortcuts import render
from cursor_django.settings import BASE_DIR

def home(request):

    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html') 

def contact(request):
    return render(request, 'contact.html')

def pricing(request):
    return render(request, 'pricing.html')

def products(request):
    return render(request, 'products.html')