from django.contrib import admin

from . import models


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile']
    list_per_page = 20
    list_select_related = ['profile']
    ordering = ['title']
    search_fields = ['title']


@admin.register(models.PostComment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'post', 'profile']
    list_per_page = 20
    list_select_related = ['post', 'profile']
    ordering = ['profile']
    search_fields = ['comment']
