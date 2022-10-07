""" Core Signals """
from django.conf import settings
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.response import Response
import cloudinary
from ..models import Profile
from . import media_uploaded, instance_deleted


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    """ Signal to create profile on user creation """
    Profile.objects.create(user=instance)


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    """ Signal to delete user on profile deletion """
    user = instance.user
    user.delete()
    cloudinary.uploader.destroy(str(user))

    return Response("User has been successfully deleted")


@receiver(media_uploaded)
def delete_previous_image_cloudinary(sender, **kwargs):
    """ Signal to delete previous image on cloudinary """
    cloudinary.uploader.destroy(str(kwargs['image']))


@receiver(instance_deleted)
def delete_instance_image_cloudinary(sender, **kwargs):
    cloudinary.uploader.destroy(str(kwargs['image']))
