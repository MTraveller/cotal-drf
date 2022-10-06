""" Core App Models """
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify


class User(AbstractUser):
    email = models.EmailField(unique=True)


def user_directory_path(instance, filename):
    """
    file/image will be uploaded to 
    MEDIA_ROOT/user_<id>/instance/<filename>
    """
    # Source:
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.FileField.upload_to
    return f'user_{0}/{1}/{2}'.format(instance.user.id, instance, filename)


class Profile(models.Model):
    """
    Profile model
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField()
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)

    class Status(models.TextChoices):
        """
        Profile Status Choices
        """
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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)


class Linktree(models.Model):
    """
    Profile Linktree model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='linktrees')
    title = models.CharField(max_length=8, default='Linktree')
    username = models.CharField(max_length=50)


class Social(models.Model):
    """
    Profile Social link model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='socials')

    # Easily adding TextChoices source:
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
    class SocialMedia(models.TextChoices):
        """
        User Profile Social Choices
        """
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
    username = models.CharField(max_length=50)


class Portfolio(models.Model):
    """
    Profile Portfolio model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='portfolios')
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)


class Award(models.Model):
    """
    Profile Award model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='awards')
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)


class Certificate(models.Model):
    """
    Profile Certificate model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='certificates')
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)


class Creative(models.Model):
    """
    Profile Creative model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='creatives')
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)


class Setting(models.Model):
    """
    User Profile Settings
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='settings')
