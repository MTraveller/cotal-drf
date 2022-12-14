""" Core Signals """
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import cloudinary
import cloudinary.api
from profiles.models import *
from . import (
    profile_deleted, media_uploaded,
    instance_deleted, profile_connect
)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    """ Signal to create profile on user creation """
    if not instance.is_superuser or not instance.is_staff:
        Profile.objects.create(id=instance.id, user_id=instance.id)
        Setting.objects.create(profile_id=instance.id)


@receiver(post_delete, sender=Profile)
def delete_user(sender, instance, **kwargs):
    """ Signal to delete user on profile deletion """
    user = instance.user
    user.delete()


@receiver(profile_deleted)
def delete_user_cloudinary(sender, **kwargs):
    user_root_folder = f"\
        {settings.MEDIA_URL}user_{str(kwargs['user'])}"\
        [1:]

    user_folders = cloudinary.api.subfolders(
        f"{settings.MEDIA_URL}user_{str(kwargs['user'])}"
    )['folders']

    for folder in user_folders:
        path = folder['path']

        try:
            cloudinary.api.delete_folder(folder['path'])
        except cloudinary.exceptions.BadRequest:  # type: ignore

            folder_resources = cloudinary.api.resources(
                type='upload', prefix=path)

            for asset in folder_resources['resources']:
                cloudinary.uploader.destroy(asset['public_id'])  # type: ignore

            cloudinary.api.delete_folder(folder['path'])

    cloudinary.api.delete_folder(user_root_folder)


@receiver(media_uploaded)
def delete_previous_image_cloudinary(sender, **kwargs):
    """ Signal to delete previous image on cloudinary """
    cloudinary.uploader.destroy(str(kwargs['image']))  # type: ignore


@receiver(instance_deleted)
def delete_instance_image_cloudinary(sender, **kwargs):
    cloudinary.uploader.destroy(str(kwargs['image']))  # type: ignore


# Due to deadline this is a future feature
# Signal to send email on connect
@receiver(profile_connect)
def initiate_profile_connect(sender, **kwargs):
    return
