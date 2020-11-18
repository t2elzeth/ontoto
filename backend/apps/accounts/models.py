from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, password, **kwargs):
        """
        Creates and saves a User with the given email and password.
        """
        email = kwargs.get('email')
        if not email:
            raise ValueError('Users must have an email address')

        kwargs['email'] = self.normalize_email(email)

        user = self.model(
            **kwargs
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **data):
        email = data.get('email')
        password = data.get('password')
        user = self.model(
            email=email,
            phone=email
        )

        user.set_password(password)
        user.is_superuser = True
        user.is_staff = True
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

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now=True)
    confirmed = models.BooleanField(default=False)

    description = models.TextField(blank=True, null=True)
    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

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
