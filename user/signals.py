""" User Signals """
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile


USER = settings.AUTH_USER_MODEL


@receiver(post_save, sender=USER)
def create_profile(sender, instance, **kwargs):
    """ Signal to create profile on user creation """
    Profile.objects.create(user=instance)
