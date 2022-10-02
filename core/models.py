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
    return f'user_{0}/{1}'.format(instance.user.id, filename)


class Profile(models.Model):
    """ Profile model """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True)

    class Status(models.TextChoices):
        """ Profile Status Choices """
        EMPLOYEE = 'EP', _('Employee')
        JOB_SEEKER = 'JS', _('Job Seeker')
        OPEN_TO_COLLABORATE = 'OC', _('Open To Collaborate')
        OWNER = 'OW', _('Owner')

    status = models.CharField(
        max_length=2, blank=True, null=True, choices=Status.choices)
    location = models.CharField(max_length=255, blank=True, null=True)


class Link(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='links')
    title = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True, validators=[URLValidator])


class Social(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='socials')

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

    name = models.CharField(max_length=10, blank=True, null=True, choices=SocialMedia.choices)
    username = models.CharField(max_length=255, blank=True, null=True)
