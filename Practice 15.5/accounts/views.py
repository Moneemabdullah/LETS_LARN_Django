from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from .forms import SignUpForm, CustomPasswordChangeForm

# Home View
def home(request):
    return render(request, 'accounts/home.html')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# Profile View
@login_required
def profile(request):
    messages.success(request, 'Logged In Successfully')
    return render(request, 'accounts/profile.html')

# Logout View
def logout_view(request):
    messages.success(request, 'Logged Out Successfully')
    return auth_views.LogoutView.as_view()(request)