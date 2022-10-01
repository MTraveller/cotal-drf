""" UserProfile App Models """
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


class ProfileLink(models.Model):
    """ User Profile Link class """

    class Link(models.TextChoices):
        """ User Profile Link Choices """
        INSTAGRAM = 'IG', _('Instagram')
        FACEBOOK = 'FB', _('Facebook')
        TWITTER = 'TW', _('Twitter')
        SNAPCHAT = 'SP', _('Snapchat')
        TIKTOK = 'TT', _('TikTok')
        TELEGRAM = 'TG', _('Telegram')
        DRIBBLE = 'DB', _('Dribble')
        PINTEREST = 'PT', _('Pinterest')
        REDDIT = 'RD', _('Reddit')
        SOUNDCLOUD = 'SC', _('SoundCloud')
        DEVIANTART = 'DA', _('DeviantArt')

        __empty__ = _('(Unknown)')

    external = models.CharField(max_length=200, validators=[URLValidator])
    social = models.CharField(
        max_length=2, choices=Link.choices, default=Link.__empty__)


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

        __empty__ = _('(Unknown)')

    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.__empty__)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    link = models.ForeignKey(ProfileLink, blank=True, null=True, on_delete=models.CASCADE)
