from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, 'webapp/index3.html')

def index_ru(request):
    return render(request, 'webapp/index_ru.html')

def portfolio(request):
    return render(request, 'webapp/portfolio.html')       




