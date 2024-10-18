from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from posts.models import Post
from .forms import UserProfileForm
from .models import UserProfile


# Create your views here.
def user_profile(request, username):
    user_prof = User.objects.get(username=username)
    user_posts = Post.objects.filter(user=user_prof)
    return render(request, 'user_profiles/user_profile.html', {'user_profile': user_prof, 'user_posts': user_posts})


def edit_profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('user_profile', username=request.user.username)
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'user_profiles/edit_profile.html', {'form': form})


