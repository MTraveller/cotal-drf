from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.defaultfilters import slugify


# https://docs.djangoproject.com/en/4.1/topics/db/managers/#custom-managers
class TaggedItemManager(models.Manager):
    """
    Class to overwrite the default object manager.
    """

    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        return TaggedItem.objects \
            .select_related('tag') \
            .filter(
                content_type=content_type,
                object_id=obj_id
            )


class Tag(models.Model):
    """
    Tag model to store all tags made by all users.
    """
    label = models.CharField(max_length=50)
    slug = models.SlugField(blank=True)

    def __str__(self) -> str:
        return self.label

    def save(self, *args, **kwargs):
        self.slug = slugify(self.label)
        super().save(*args, **kwargs)


# https://docs.djangoproject.com/en/4.1/ref/contrib/contenttypes/#overview
class TaggedItem(models.Model):
    """
    TaggedItem model to store information about
    tagged posts and which tags.
    """
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name='tags')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
