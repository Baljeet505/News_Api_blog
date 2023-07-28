# news_api_app/views.py

from django.shortcuts import render
from django.conf import settings
import requests
from .models import NewsArticle

def index(request):
    url = 'https://newsapi.org/v2/top-headlines'
    params = {
        'country': 'us',  # Replace with your desired country or other filters
        'apiKey': settings.NEWS_API_KEY,
    }

    response = requests.get(url, params=params)
    data = response.json()

    articles = []

    if response.status_code == 200 and data['status'] == 'ok':
        for article in data['articles']:
            news_article = NewsArticle(
                title=article['title'],
                description=article['description'],
                url=article['url'],
                published_at=article['publishedAt'],
                image_url=article.get('urlToImage'),
            )
            articles.append(news_article)

    return render(request, 'NewsApp/index.html', {'articles': articles})
