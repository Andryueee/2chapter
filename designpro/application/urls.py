from django.urls import path, re_path
from . import views

from django.contrib import admin
urlpatterns = [
   path('', views.application_home, name='application_home'),


   re_path('create/', views.create, name='create'),



   path('<int:pk>/', views.ApplicationDetailView.as_view(), name='application-detail'),
   path('<int:pk>/update/', views.ApplicationUpdateView.as_view(), name='application-update'),
   path('<int:pk>/delete/', views.ApplicationDeleteView.as_view(), name='application-delete')
]
