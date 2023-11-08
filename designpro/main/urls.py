from django.urls import path, include
from . import views
from django.urls import re_path

from django.contrib import admin
urlpatterns = [
   path('catalog/', views.index),
   path('about/', views.about),
   re_path(r'^register/$', views.register, name='register'),

]

from .views import *

urlpatterns += [
   re_path('user_profile/<int:pk>/', ShowProfilePageView.as_view(), name='user_profile'),

]


