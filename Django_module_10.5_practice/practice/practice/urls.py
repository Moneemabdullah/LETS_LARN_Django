from django.contrib import admin
from django.urls import path, include
from practice.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('first_app/', include('first_app.urls')),
]
