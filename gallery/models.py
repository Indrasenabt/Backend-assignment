from django.db import models
from django.contrib.auth.models import User

class FavoriteImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites')
    image_url = models.URLField(max_length=500)
    breed = models.CharField(max_length=100, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    tags = models.JSONField(default=list, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s favorite - {self.breed or 'Unknown Breed'}"

