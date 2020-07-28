from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, 'webapp/index.html')

# def index_ru(request):
#     return render(request, 'webapp/index_ru.html')

def about(request):
    return render(request, 'webapp/about.html')

def portfolio(request):
    return render(request, 'webapp/portfolio.html')

def contact(request):
    return render(request, 'webapp/contact.html')

# def services(request):
#     return render(request, 'webapp/services.html')        

def example_1(request):
    return render(request, 'webapp/portfolio/example_1.html')             

def example_2(request):
    return render(request, 'webapp/portfolio/example_2.html')    

def example_3(request):
    return render(request, 'webapp/portfolio/example_3.html')    

def example_4(request):
    return render(request, 'webapp/portfolio/example_4.html')    

def example_5(request):
    return render(request, 'webapp/portfolio/example_5.html') 

def example_6(request):
    return render(request, 'webapp/portfolio/example_6.html')    


