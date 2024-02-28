from django_use_email_as_username.models import BaseUser, BaseUserManager
from django.db import models


class User(BaseUser):
    objects = BaseUserManager()
    phone = models.CharField(max_length=250, blank=True, null=True)
