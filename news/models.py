from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FavoriteQuery(models.Model):
    query = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.query} (par {self.user.username})"