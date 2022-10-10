from django.db import models
from django.template.defaultfilters import slugify
from core.upload_to import user_directory_path
from profiles.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profileposts')

    title = models.CharField(max_length=80)
    post = models.TextField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PostImage(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='postimages')

    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)


class PostComment(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profilecomments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='postcomments')

    comment = models.CharField(max_length=300)
