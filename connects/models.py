from django.db import models
from django.utils.translation import gettext_lazy as _
from core.signals import profile_connect
from profiles.models import Profile


# https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#generic-relations
class Connected(models.Model):
    connecter = models.ForeignKey(Profile,
                                  on_delete=models.CASCADE, related_name='connecter')
    connecting = models.ForeignKey(Profile,
                                   on_delete=models.CASCADE, related_name='connecting')

    class Connect(models.TextChoices):
        NO = 0, _('0')
        Yes = 1, _('1')

    connecter_choice = models.CharField(
        max_length=1, choices=Connect.choices, default=Connect.NO)
    connecting_choice = models.CharField(
        max_length=1, choices=Connect.choices, default=Connect.NO)

    def save(self, *args, **kwargs):
        profile_connect.send_robust(self.__class__, self_dict=self.__dict__)
        super().save(*args, **kwargs)
