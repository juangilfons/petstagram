from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from accounts.forms import RegisterForm

from user_profiles.models import UserProfile


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'authenticate/login.html'

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('posts')

    else:
        form = RegisterForm()
    return render(request, 'authenticate/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
