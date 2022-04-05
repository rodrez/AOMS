from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import AomsUserManager


class AomsUser(AbstractUser):

    username = None
    email = models.EmailField(_("email_address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = AomsUserManager()

    def __str__(self):
        return self.email
