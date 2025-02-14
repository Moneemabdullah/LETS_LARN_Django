from django.urls import path 
from model_form.views import model_form
urlpatterns = [
    path('', model_form, name='model_form')
]
