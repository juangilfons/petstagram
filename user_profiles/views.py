from django.contrib.auth.models import User
from django.shortcuts import render

from posts.models import Post


# Create your views here.
def user_profile(request, username):
    user_prof = User.objects.get(username=username)
    user_posts = Post.objects.filter(user=user_prof)
    return render(request, 'user_profiles/user_profile.html', {'user_profile': user_prof, 'user_posts': user_posts})
