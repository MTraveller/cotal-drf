""" User Profile Upload To Function """
from .signals import media_uploaded


def user_directory_path(instance, filename):
    """
    file/image will be uploaded to 
    MEDIA_ROOT/user_<id>/instance/<filename>
    """
    # Source:
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.upload_to
    previous_image = instance.__class__.objects.get(
        id=instance.id).image

    if previous_image:
        media_uploaded.send_robust(
            instance.__class__, image=previous_image)

    instance_name = instance.__class__.__name__.lower()

    if instance_name == 'profile':
        return '{0}/{1}/{2}'.format(
            instance.slug, instance_name, filename
        )

    return '{0}/{1}/{2}'.format(
        instance.profile.slug, instance_name, filename
    )
