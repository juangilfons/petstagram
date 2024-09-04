from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Post
# Create your views here.

@login_required
def posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/posts.html', {'posts': posts})

@login_required
def upload_post(request):
    pass

@login_required
def post_detail(request, post_id):
    pass
