from django.db import models


class Post(models.Model):
    profile = models.ForeignKey()
    content = models.CharField(max_length=1500)


class PostImage(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='post-images')


class Comment(models.Model):
    profile = models.ForeignKey(
        on_delete=models.CASCADE, related_name='comments')
    comment = models.CharField(max_length=300)


class Like(models.Model):
    profile = models.ForeignKey(on_delete=models.CASCADE, related_name='likes')
    profile_liked = models.ForeignKey(on_delete=models.CASCADE)


class Follow(models.Model):
    profile = models.ForeignKey(
        on_delete=models.CASCADE, related_name='follows')
    profile_followed = models.ForeignKey(on_delete=models.CASCADE)
