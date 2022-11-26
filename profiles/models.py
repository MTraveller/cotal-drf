from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from core.upload_to import user_directory_path
from core.signals import profile_deleted, instance_deleted


class Profile(models.Model):
    """
    Profile model
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=80)
    image = models.ImageField(default=None,
                              upload_to=user_directory_path,
                              blank=True, null=True)

    class Status(models.TextChoices):
        """
        Profile Status Choices
        """
        # Easily adding TextChoices source:
        # https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types
        OWNER = 'Owner', _('Owner')
        EMPLOYEE = 'Employee', _('Employee')
        JOB_SEEKER = 'Job Seeker', _('Job Seeker')
        OPEN_TO_COLLABORATE = 'Open To Collaborate', _('Open To Collaborate')
        HANDS_FULL = 'Hands Full', _('Hands Full')
        TRAVELING = 'Traveling', _('Traveling')
        NOT_SPECIFIED = 'Not Specified', _('Not Specified')

    status = models.CharField(blank=True, null=True,
                              max_length=19, choices=Status.choices,
                              default=Status.NOT_SPECIFIED
                              )
    location = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        profile_deleted.send_robust(
            self.__class__, user=self.user_id)  # type: ignore
        super().delete(*args, **kwargs)


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
        DEVIANTART = 'DeviantArt', _('DeviantArt')
        DRIBBLE = 'Dribble', _('Dribble')
        GITHUB = 'GitHub', _('GitHub')
        SOUNDCLOUD = 'SoundCloud', _('SoundCloud')
        PINTEREST = 'Pinterest', _('Pinterest')

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
    slug = models.SlugField(max_length=80)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for ordering by created on"""
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        instance_deleted.send_robust(
            self.__class__, image=self.image)
        super().delete(*args, **kwargs)


class Award(models.Model):
    """
    Profile Award model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='awards')
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=80)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for ordering by created on"""
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        instance_deleted.send_robust(
            self.__class__, image=self.image)
        super().delete(*args, **kwargs)


class Certificate(models.Model):
    """
    Profile Certificate model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='certificates')
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=80)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for ordering by created on"""
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        instance_deleted.send_robust(
            self.__class__, image=self.image)
        super().delete(*args, **kwargs)


class Creative(models.Model):
    """
    Profile Creative model
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='creatives')
    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=80)
    description = models.CharField(max_length=500)
    link = models.URLField(max_length=255, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta class for ordering by created on"""
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        instance_deleted.send_robust(
            self.__class__, image=self.image)
        super().delete(*args, **kwargs)


class Setting(models.Model):
    """
    User Profile Settings
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='settings')

    class Activity(models.TextChoices):
        """
        User Profile Activity Choices
        """
        SHOW = 1, _('Show')
        HIDE = 0, _('Hide')

    title = models.CharField(max_length=16, default='Profile Activity')
    activity = models.CharField(
        max_length=1, choices=Activity.choices, default=Activity.SHOW)
