from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from . import managers


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model for authentication"""
    objects = managers.UserManager()

    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=255, default="")
    full_name = models.CharField(max_length=255, default="")
    description = models.TextField(default="")

    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    # No longer need in usernames, email is enough to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Email & Password are required by default.

    def get_username(self):
        """Returns field used for authentication"""
        return getattr(self, self.USERNAME_FIELD)

    def get_full_name(self):
        """Returns full name of user"""
        return self.full_name

    def __str__(self):
        """What to display in admin panel"""
        return self.get_username()
