from django.urls import path

from . import views

urlpatterns = [
    path('', views.posts, name='posts'),
    path('upload/', views.upload_post, name='upload_post'),
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),
]