import datetime

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, password, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        email = kwargs.get('email')

        kwargs['email'] = self.normalize_email(email)

        user = self.model(**kwargs)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **data):
        """
        Creates and saves a superuser with the given email and password
        """
        password = data.get('password')

        data = self.model.prettify_data(data, for_superuser=True)

        user = self.model(**data)

        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(blank=True, null=True)
    date_joined = models.DateTimeField()
    confirmed = models.BooleanField(default=False)

    description = models.TextField(blank=True, null=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    def update_last_login(self):
        self.last_login = datetime.datetime.now()
        self.save()

    @staticmethod
    def prettify_data(data, for_superuser=False):
        """
        Filters the data in `validated_data`
        so that it can be passed to the `User` model
        """
        current_date = timezone.now()

        # Remove unnecessary data
        data.pop('password', None)
        data.pop('password2', None)

        # Check if full_name is given
        if for_superuser:
            data.update({
                'full_name': 'SuperUser. No full name specified',
                'phone': '',
                'is_superuser': True,
                'is_staff': True
            })

        # Add required data
        data.update({
            'last_login': current_date,
            'date_joined': current_date
        })

        return data

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
