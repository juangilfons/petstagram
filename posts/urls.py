from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('upload/', views.upload_post, name='upload_post'),
]