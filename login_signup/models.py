from django.db import models

from django.contrib.auth.models import Permission, User
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    is_client = models.BooleanField(default=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True, default = 'user_pic/avatar.png')
