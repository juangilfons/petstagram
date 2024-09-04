from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout

from accounts.forms import RegisterForm


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'authenticate/login.html'

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegisterForm()
    return render(request, 'authenticate/register.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('login')
