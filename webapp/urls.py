from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('ru', views.index_ru, name='index_ru'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('portfolio/example-1', views.example_1, name='example_1'),
]


