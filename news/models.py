from django.db import models

# Create your models here.
class FavoriteQuery(models.Model):
    query = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query