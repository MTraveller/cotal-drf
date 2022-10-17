""" Core Signals """
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
import cloudinary
import cloudinary.api
from ..initial_db import do_initial_db_populate
from profiles.models import *
from . import (
    initial_db,
    profile_deleted, media_uploaded,
    instance_deleted, profile_connect
)


# Hack for adding initial db record for all models
# for grapghQL to use on the frontend and by pass not shown
# query options on build time
@receiver(initial_db)
def create_initial_db_for_frontend_graph_ql(sender, **kwargs):
    return do_initial_db_populate(**kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, **kwargs):
    """ Signal to create profile on user creation """
    Profile.objects.create(user=instance)
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


@receiver(profile_connect)
def initiate_profile_connect(sender, **kwargs):
    print("Connecting")
