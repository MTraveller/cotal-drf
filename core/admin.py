from django.contrib import admin
from . import models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'is_active']
    list_filter = ['is_active']
    list_per_page = 20
    ordering = ['first_name', 'last_name']
    search_fields = ['username__istartswith']

    def user_name(self, user):
        return f'{user.first_name} {user.last_name}'
