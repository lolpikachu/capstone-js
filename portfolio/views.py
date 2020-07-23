from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse



def portfolio(request):
    return render(request, 'portfolio.html')   