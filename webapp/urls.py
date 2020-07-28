from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('ru', views.index_ru, name='index_ru'),
    # path('ru', views.index_ru, name='index_ru'),
    # path('portfolio', views.portfolio, name='portfolio'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    # path('services', views.services, name='services'),
    # path('about', views.about, name='about'),
    path('portfolio/work-1', views.example_1, name='example_1'),
    path('portfolio/work-2', views.example_2, name='example_2'),
    path('portfolio/work-3', views.example_3, name='example_3'),
    path('portfolio/work-4', views.example_4, name='example_4'),
    path('portfolio/work-5', views.example_5, name='example_5'),
    path('portfolio/work-6', views.example_6, name='example_6'),
]


