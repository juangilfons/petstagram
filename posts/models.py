import os
from django.db import models
from django.utils import timezone
from datetime import timedelta

from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='images/')
    caption = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)

    class Meta:
        ordering = ['-created_at']

    def time_since_post(self):
        now = timezone.now()
        time_diff = now - self.created_at

        if time_diff < timedelta(hours=1):
            minutes = time_diff.seconds // 60
            return f"{minutes} mins ago"
        elif time_diff < timedelta(hours=24):
            hours = time_diff.seconds // 3600
            return f"{hours} hrs ago"
        else:
            days = time_diff.days
            return f"{days} days ago"

    def delete(self, *args, **kwargs):
        if self.image:
            if os.path.isfile(self.image.path):
                os.remove(self.image.path)
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username}'s Post"
