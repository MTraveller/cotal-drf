from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
from core.upload_to import user_directory_path
from profiles.models import Profile
from tags.models import TaggedItem


class Post(models.Model):
    """
    Post model stores profile, post details and
    has a generic relation to TaggedItem model.
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profileposts')

    image = models.ImageField(
        upload_to=user_directory_path, blank=True, null=True)
    title = models.CharField(max_length=80)
    post = models.TextField()
    slug = models.SlugField(max_length=80)
    created_on = models.DateTimeField(auto_now_add=True)

    tags = GenericRelation(TaggedItem, related_query_name='tags')

    class Meta:
        """Meta class for ordering by created on"""
        ordering = ['-created_on']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class PostComment(models.Model):
    """
    Post comment model stores user, post which the comment
    were made on and the comment.
    """
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='profilecomments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='postcomments')
    created_on = models.DateTimeField(auto_now_add=True)

    comment = models.CharField(max_length=300)

    class Meta:
        """Meta class for ordering by created on"""
        ordering = ['-created_on']
