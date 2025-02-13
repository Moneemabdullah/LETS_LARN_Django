from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('about/', views.about, name='aboutpage'),
    path('form/', views.submit_form, name='form'),
    path('django_form/', views.django_form, name='django_form'),
]
