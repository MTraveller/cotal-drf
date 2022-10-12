from django.db import models
from django.utils.translation import gettext_lazy as _
from profiles.models import Profile


class Followed(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='follows')
    followed_by = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, related_name='followedby')

    followed_by_username = models.CharField(max_length=150)

    class Follow(models.TextChoices):
        NO = 0, _('0')
        Yes = 1, _('1')

    follower_choice = models.CharField(
        max_length=1, choices=Follow.choices, default=Follow.NO)
