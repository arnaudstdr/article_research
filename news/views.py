from django.shortcuts import render
import requests
from datetime import datetime, timedelta
from django.conf import settings

# Create your views here.
def search_news_view(request):
    api_key = settings.NEWS_API_KEY
    query = '"machine learning" OR "deep learning" OR "intelligence artificielle" OR "cybersécurité" OR "programmation" OR "open source"'
    to_date = datetime.today().strftime('%Y-%m-%d')
    from_date = (datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d')

    url = 'https://newsapi.org/v2/everything'
    params = {
        'q': query,
        'from': from_date,
        'to': to_date,
        'language': 'fr',
        'sortBy': 'relevance',
        'apiKey': api_key,
        'pageSize': '50'
    }

    response = requests.get(url, params=params)
    articles = response.json().get('articles', [] if response.status_code == 200 else [])

    # Rue par date côté serveur si la date publication existe
    articles = sorted(
        articles,
        key=lambda article: article.get('publishedAt'),
        reverse=True # Du plus récent au plus ancien
    )
    return render(request, 'news/search_news.html', {'articles': articles})