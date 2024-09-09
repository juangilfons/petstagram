from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.
def user_profile(request, user_id):
    user_profile = User.objects.get(pk=user_id)
    return render(request, 'user_profiles/user_profile.html', {'user_profile': user_profile})
