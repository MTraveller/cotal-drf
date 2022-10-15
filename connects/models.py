from django.db import models
from django.utils.translation import gettext_lazy as _
from core.signals import profile_connect
from profiles.models import Profile


class Connected(models.Model):
    """
    Connected model to connect two profiles, while
    the connecter initiates the connection and the
    connecting either accepts the connection or igores it.
    """
    connecter = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='connecters')
    connecting = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='connectings')

    connecter_username = models.CharField(max_length=150)

    class Connect(models.TextChoices):
        IGNORE = 0, _('0')
        CONNECT = 1, _('1')
        UNSPECIFIED = 2, _('2')

    connecter_choice = models.CharField(
        max_length=1, choices=Connect.choices, default=Connect.UNSPECIFIED)
    connecting_choice = models.CharField(
        max_length=1, choices=Connect.choices, default=Connect.UNSPECIFIED)

    def save(self, *args, **kwargs):
        profile_connect.send_robust(
            self.__class__, selfdict=self.__dict__, **kwargs)
        super().save(*args, **kwargs)
