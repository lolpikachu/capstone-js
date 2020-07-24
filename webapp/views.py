from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, 'webapp/index.html')

def about(request):
    return render(request, 'webapp/about.html')

def portfolio(request):
    return render(request, 'webapp/portfolio.html')

def contact(request):
    return render(request, 'webapp/contact.html')

def services(request):
    return render(request, 'webapp/services.html')        

def example_1(request):
    return render(request, 'webapp/portfolio/example_1.html')             




