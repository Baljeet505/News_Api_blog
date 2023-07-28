# news_api_app/models.py

from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    url = models.URLField()
    published_at = models.DateTimeField()
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
