from django.urls import path
from . import views
from django.urls import re_path

from django.contrib import admin
urlpatterns = [
   path('', views.application_home, name='application_home'),
   re_path('create/', views.create, name='create'),
   path('<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail')

]
