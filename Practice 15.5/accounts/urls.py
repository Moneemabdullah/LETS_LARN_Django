from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Import auth_views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),  # Custom logout view
    path('profile/', views.profile, name='profile'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='accounts/password_change.html',
        form_class=views.CustomPasswordChangeForm,  # Use the custom form
        success_url='/accounts/profile/'  # Redirect to profile after password change
    ), name='password_change'),
]