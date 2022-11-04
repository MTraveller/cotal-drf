from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    User model to extend the base user model.
    """
    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = ['username', 'password', 'first_name',
                       'last_name']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
