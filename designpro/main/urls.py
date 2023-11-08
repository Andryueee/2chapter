from django.urls import path, include
from . import views
from django.urls import re_path

from django.contrib import admin
urlpatterns = [
   path('catalog/', views.index),
   path('about/', views.about),
   re_path(r'^register/$', views.register, name='register'),



]


