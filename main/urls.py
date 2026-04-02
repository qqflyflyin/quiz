'''Управление ссылками'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('register', views.registration, name='registration'),
    path('game', views.game, name='game'),
    path('contacts', views.contacts, name='contacts'),
]
