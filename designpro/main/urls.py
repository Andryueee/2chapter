from django.urls import path, include
from . import views
from django.urls import re_path

from django.contrib import admin
urlpatterns = [
   path('', views.index, name='home'),
   re_path(r'^register/$', views.register, name='register'),





   path('about/', views.about),

]

from .views import *

urlpatterns += [
   path('profile/', views.ShowProfilePageView, name='user_profile'),

]



