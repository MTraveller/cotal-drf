from django.contrib import admin

from . import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'is_active']
    list_filter = ['user__is_active']
    list_per_page = 20
    list_select_related = ['user']
    ordering = ['user']
    search_fields = ['slug__istartswith']

    def name(self, profile):
        return f'{profile.user.first_name} {profile.user.last_name}'

    def is_active(self, profile):
        return profile.user.is_active


@admin.register(models.Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile']
    list_per_page = 20
    ordering = ['title']
    search_fields = ['title']


@admin.register(models.Award)
class AwardAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile']
    ordering = ['title']
    list_per_page = 20
    search_fields = ['title']


@admin.register(models.Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile']
    ordering = ['title']
    list_per_page = 20
    search_fields = ['title']


@admin.register(models.Creative)
class CreativeAdmin(admin.ModelAdmin):
    list_display = ['title', 'profile']
    ordering = ['title']
    list_per_page = 20
    search_fields = ['title']
