from django.urls import path
from .views import search_news_view

urlpatterns = [
    path('search/', search_news_view, name='search_news'),
]