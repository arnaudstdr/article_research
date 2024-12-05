from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_news, name='search_news'),
path('delete_favorite/<int:favorite_id>/', views.delete_favorite, name='delete_favorite'),
]