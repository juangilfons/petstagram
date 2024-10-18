import os
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default_image/default.jpg')
    bio = models.TextField(default="")
    followers = models.ManyToManyField('self', symmetrical=False,  related_name='following', blank=True)

    def __str__(self):
        return self.user.username

    def follow(self, profile):
        self.followers.add(profile)

    def unfollow(self, profile):
        self.followers.remove(profile)

    def is_following(self, profile):
        self.followers.filter(id=profile).exists()

    def followers_count(self):
        self.followers.count()

    def following_count(self):
        self.following.count()

    def save(self, *args, **kwargs):
        if self.pk:
            old_profile = UserProfile.objects.get(pk=self.pk)
            if old_profile.profile_picture and self.profile_picture != old_profile.profile_picture:
                default_image_path = os.path.join(settings.MEDIA_ROOT, settings.DEFAULT_PROFILE_PICTURE)
                old_image_path = os.path.join(settings.MEDIA_ROOT, old_profile.profile_picture.path)
                if os.path.isfile(old_image_path) and old_image_path != default_image_path:
                    os.remove(old_image_path)

        super().save(*args, **kwargs)
