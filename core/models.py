""" Core App Models """
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.core.validators import URLValidator


class User(AbstractUser):
    email = models.EmailField(unique=True)


def user_directory_path(instance, filename):
    """ file/image will be uploaded to MEDIA_ROOT/user_<id>/<filename> """
    # Source:
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.upload_to
    return f'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    """ Profile model """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)

    class Status(models.TextChoices):
        """ Profile Status Choices """
        # Easily adding TextChoices source:
        # https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
        EMPLOYEE = 'Employee', _('Employee')
        JOB_SEEKER = 'Job Seeker', _('Job Seeker')
        OPEN_TO_COLLABORATE = 'Open To Collaborate', _('Open To Collaborate')
        OWNER = 'Owner', _('Owner')

        __empty__ = _('Not Specified')

    status = models.CharField(
        max_length=19, choices=Status.choices, default=Status.__empty__, null=True)
    location = models.CharField(max_length=255, null=True)


class Link(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255, validators=[URLValidator])


class Social(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='socials')

    # Easily adding TextChoices source:
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
    class SocialMedia(models.TextChoices):
        """ User Profile Link Choices """
        INSTAGRAM = 'Instagram', _('Instagram')
        FACEBOOK = 'Facebook', _('Facebook')
        TWITTER = 'Twitter', _('Twitter')
        SNAPCHAT = 'Snapchat', _('Snapchat')
        TIKTOK = 'TikTok', _('TikTok')
        TELEGRAM = 'Telegram', _('Telegram')
        DRIBBLE = 'Dribble', _('Dribble')
        PINTEREST = 'Pinterest', _('Pinterest')
        REDDIT = 'Reddit', _('Reddit')
        SOUNDCLOUD = 'SoundCloud', _('SoundCloud')
        DEVIANTART = 'DeviantArt', _('DeviantArt')

    name = models.CharField(max_length=10, choices=SocialMedia.choices)
    username = models.CharField(max_length=255)


class Follow(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='follows')
    username = models.CharField(max_length=255)
