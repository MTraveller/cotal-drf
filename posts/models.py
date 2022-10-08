import profile
from django.db import models
from django.template.defaultfilters import slugify
from core.upload_to import user_directory_path
from profiles.models import Profile


class Post(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='posts')

    title = models.CharField(max_length=80)
    post = models.TextField()
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PostImage(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='postimages')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)


class Comment(models.Model):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='postcomments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    comment = models.CharField(max_length=300)
