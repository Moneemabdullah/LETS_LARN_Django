from django.urls import path, include
from . import views

urlpatterns = [
    path('about/', views.about),
    path('contuct/', views.contuct),
]
