from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'portal'

urlpatterns = [
   # post views
   path('', views.home, name='home'),
   path('search/', views.search, name='search'),
   path('about/', views.about, name='about'),
   path('scrap/', views.scrap, name='scrap'),
   path('category_list/', views.category_list, name='category_list'),
   path('<slug:category_slug>/', views.home, name='job_list_by_category'),
   
]