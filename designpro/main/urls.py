from django.urls import path, include
from . import views
from django.urls import re_path

from django.contrib import admin
urlpatterns = [
   path('catalog/', views.index, name='home'),
   path('about/', views.about),
   re_path(r'^register/$', views.register, name='register'),

]

from .views import *

urlpatterns += [
   path('profile/', views.ShowProfilePageView, name='user_profile'),

]


urlpatterns += [
   re_path('create/', views.create, name='create')

]

