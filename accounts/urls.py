from django.urls import path
from . import views

urlpatterns = [
    path('login_user/', views.CustomLoginView.as_view(), name='login'),
    path('register_user/', views.register_user, name='register'),
]
