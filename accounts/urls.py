from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
from .forms import CustomLoginForm

urlpatterns = [
   # post views
   # path('login/', views.user_login, name='login'),
   path('login/', auth_views.LoginView.as_view(authentication_form=CustomLoginForm), name='login'),
   path('logout/', auth_views.LogoutView.as_view(), name='logout'),
   path('register/', views.register, name='register'),
   path('profile/', views.profile, name='profile'),  
   path('profile_edit/', views.profile_edit, name='profile_edit'),  
]