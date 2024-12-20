from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import requests
from django.conf import settings
from .models import FavoriteQuery

# Create your views here.
@login_required
def search_news(request):
    query = request.GET.get('query', '')
    articles = []
    favorites = FavoriteQuery.objects.filter(user=request.user)

    if query:
        api_key = settings.NEWS_API_KEY
        url = f'https://newsapi.org/v2/everything?q={query}&language=fr&apiKey={api_key}'
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                articles = data.get('articles', [])
            else:
                print(f"Erreur API: {response.status_code} - {response.text}")
        except Exception as e:
            print(f"Erreur lors de la requête API: {e}")

    if 'add_favorite' in request.GET and query:
        if not FavoriteQuery.objects.filter(user=request.user, query=query).exists():
            FavoriteQuery.objects.create(user=request.user, query=query)
        return redirect('search_news')

    articles = sorted(
        articles,
        key=lambda article: article.get('publishedAt'),
        reverse=True  # Du plus récent au plus ancien
    )

    return render(request, 'news/search_news.html', {
        'articles': articles,
        'query': query,
        'favorites': favorites,
    })

@login_required
def delete_favorite(request, favorite_id):
    try:
        favorite = FavoriteQuery.objects.get(id=favorite_id, user=request.user)
        favorite.delete()
    except FavoriteQuery.DoesNotExist:
        return HttpResponseForbidden("Vous n'avez pas la permission de supprimer ce favori.")
    return redirect('search_news')

