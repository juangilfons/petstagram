import os

from datetime import timezone

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


from .forms import PostForm
from .models import Post
from .image_validation import detect_pet
# Create your views here.

@login_required
def posts(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts.html', {'posts': posts})

@login_required
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            temp_image_path = default_storage.save('temp_images/' + image.name, ContentFile(image.read()))
            temp_image_full_path = os.path.join(default_storage.location, temp_image_path)
            if detect_pet(temp_image_full_path):
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                default_storage.delete(temp_image_path)
                return redirect('posts')
            else:
                messages.error(request, "Please upload a valid pet photo.")
                default_storage.delete(temp_image_path)
            return render(request, 'posts/upload_post.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'posts/upload_post.html', {'form': form})