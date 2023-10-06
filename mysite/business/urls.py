from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('examples/', views.examples),
    path('contact/', views.contact)
]