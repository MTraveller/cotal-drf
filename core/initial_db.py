from django.core.exceptions import ObjectDoesNotExist
from core.models import User
from profiles.models import *
from posts.models import *
from follows.models import *
from connects.models import *
from tags.models import *


def do_initial_db_populate(**kwargs):
    print("KWARGS", kwargs)
    try:
        User.objects.get(username='initial')
    except ObjectDoesNotExist:
        print("Does not exist!!")
