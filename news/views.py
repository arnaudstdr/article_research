from django.shortcuts import render
import requests
from django.conf import settings

# Create your views here.
def search_news(request):
    # Récupérer la requête saisie dans la barre de recherche (GET request)
    query = request.GET.get('query', '')  # Par défaut, une chaîne vide si aucune requête
    articles = []
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

        articles = sorted(
            articles,
            key=lambda article: article.get('publishedAt'),
            reverse=True  # Du plus récent au plus ancien
        )

    return render(request, 'news/search_news.html', {
        'articles': articles,
        'query': query,  # Ajouter 'query' pour que la barre de recherche conserve la valeur saisie
    })

