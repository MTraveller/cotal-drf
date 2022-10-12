from django.db import models
from django.utils.translation import gettext_lazy as _
from profiles.models import Profile


class Followed(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='followers')
    followed_by = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='followings')

    followed_by_name = models.CharField(max_length=300)
    followed_by_username = models.CharField(max_length=150)
    following_by_name = models.CharField(max_length=300)
    following_by_username = models.CharField(max_length=150)

    class Follow(models.TextChoices):
        NO = 0, _('0')
        Yes = 1, _('1')

    follower_choice = models.CharField(
        max_length=1, choices=Follow.choices, default=Follow.NO)
