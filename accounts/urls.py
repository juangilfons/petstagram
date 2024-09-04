from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('login_user/', views.CustomLoginView.as_view(), name='login'),
    path('register_user/', views.register_user, name='register'),
    path('logout_user/', views.logout_user, name='logout'),
]
