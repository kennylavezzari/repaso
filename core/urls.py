from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.autoview, name='auto'),
    path('chofer', views.choferview, name='chofer'),
]