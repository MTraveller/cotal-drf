""" Core Signals """
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.response import Response
from ..models import Profile


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    """ Signal to create profile on user creation """
    Profile.objects.create(user=instance)


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    """ Signal to delete user on profile deletion """
    user = instance.user
    user.delete()

    return Response("User has been successfully deleted")
