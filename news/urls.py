from django.contrib.auth import views as auth_views
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.search_news, name='search_news'),
    path('delete_favorite/<int:favorite_id>/', views.delete_favorite, name='delete_favorite'),
    path('login/', auth_views.LoginView.as_view(template_name='news/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]