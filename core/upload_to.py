""" User Profile Upload To Function """
from .signals import media_uploaded


def user_directory_path(instance, filename):
    """
    file/image will be uploaded to 
    MEDIA_ROOT/user_<id>/instance/<filename>
    """
    # Source:
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.upload_to
    print(instance)
    print(filename)
    try:
        previous_image = instance.__class__.objects.get(
            id=instance.id).image

        print(previous_image)

        if previous_image:
            media_uploaded.send_robust(
                instance.__class__, image=previous_image)
    except:
        pass

    instance_name = instance.__class__.__name__.lower()

    print(instance_name)

    if instance_name == 'profile':
        print("PROFILE")
        return '{0}/{1}/{2}'.format(
            instance.slug, instance_name, filename
        )

    print("NOT PROFILE")
    return '{0}/{1}/{2}'.format(
        instance.profile.slug, instance_name, filename
    )
