# News App Django Project

## Description
Cette application Django permet de rechercher des articles sur des sujets précis à partir de l'API NewsAPI. Elle affiche les titres, la source, la description, l'image d'illustration et la date de publication des articles. L'application est conçue pour être simple à utiliser et peut être personnalisée pour répondre à des besoins spécifiques.

## Fonctionnalités
- Recherche d'articles par mot-clé prédéfini.
- Affichage des résultats incluant le titre, la source, la description, l'image et la date de publication.
- Utilisation de Bootstrap pour une présentation responsive et attrayante.

## Prérequis
- Python 3.8+
- Django 3.0+
- NewsAPI (clé API requise)
- Modules supplémentaires : `requests`, `python-decouple`

## Installation

1. **Cloner le répertoire**
   ```bash
   git clone https://github.com/votre-utilisateur/news-app.git
   cd news-app
   ```

2. **Créer un environnement virtuel**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Sur Windows, utiliser .venv\Scripts\activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurer la clé API**
   - Créez un fichier `.env` à la racine du projet et ajoutez votre clé API :
     ```
     NEWS_API_KEY=votre_clé_api_secrète
     ```

5. **Modifier la variable `query` dans `views.py`**
    ```python
   query = 'machine learning OR deep learning'   #exemple de sujet
   ```
6. **Migrer la base de données (si applicable)**
   ```bash
   python manage.py migrate
   ```

7. **Lancer le serveur de développement**
   ```bash
   python manage.py runserver
   ```

## Utilisation
- Accédez à l'application à l'adresse [http://127.0.0.1:8000/news/search/](http://127.0.0.1:8000/news/search/).
- La page affichera les articles liés à votre mot-clé prédéfini.

## Structure du projet
```
news_app/
|-- .venv/
|-- news/
|   |-- migrations/
|   |-- templates/
|   |   |-- news/
|   |   |   |-- search_results.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- views.py
|   |-- urls.py
|-- news_app/
|   |-- __init__.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- manage.py
|-- .env
|-- .gitignore
|-- requirements.txt
```

## Sécurité
- **Ne partagez jamais votre fichier `.env`** et veillez à ce qu'il soit ajouté à votre `.gitignore`.
- Assurez-vous de restreindre l'utilisation de votre clé API sur le tableau de bord de NewsAPI pour éviter les abus.

## Licence
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Auteur
Arnaud STADLER
Contact : arnaud.stadler@ikmail.com
