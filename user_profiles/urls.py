from django.urls import path

from . import views


urlpatterns = [
    path('edit/', views.edit_profile, name='edit_profile'),
    path('<str:username>/', views.user_profile, name='user_profile'),
]