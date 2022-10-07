""" Core Custom Signals """
from django.dispatch import Signal

# Signal for user created
user_created = Signal()

# Signal for media uploaded
media_uploaded = Signal()

# Signal for instance deleted
instance_deleted = Signal()
