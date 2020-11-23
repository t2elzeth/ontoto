from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):
    """Manager for custom User model"""
    def create_user(self, password, data):
        """Creates and saves a User with the given data"""
        data = self.model.prettify_data(data)
        user = self.model(**data)

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, **data):
        """
        Creates and saves a superuser with the given email and password

        TODO: What is difference between superusers and staff users?
        """
        password = data.get('password')

        data = self.model.prettify_data(data, for_superuser=True)

        user = self.model(**data)

        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model for authentication"""
    objects = UserManager()

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    phone = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    is_confirmed = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now())

    # No longer need in usernames, email is enough to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    @staticmethod
    def prettify_data(data, for_superuser=False):
        """
        Filters the data in `validated_data`
        so that it can be passed to the `User` model
        """
        current_date = timezone.now()
        email = data.get('email')

        # Remove unnecessary data
        data.pop('password', None)
        data.pop('password2', None)

        # Check if its for superuser
        if for_superuser:
            # Put data related only to superusers
            data.update({
                # Superuser does not really need a full name
                'full_name': 'SuperUser. No full name specified',

                # Same as full_name
                'phone': '',

                # Set only admins related fields
                'is_superuser': True,
                'is_staff': True
            })

        # Prettify existing data
        data.update({
            'email': UserManager.normalize_email(email)
        })
        return data

    def get_username(self):
        """Returns field used for authentication"""
        return getattr(self, self.USERNAME_FIELD)

    def get_full_name(self):
        """Returns full name of user"""
        return self.full_name

    def __str__(self):
        """What to display in admin panel"""
        return self.get_username()

    def has_perm(self, perm, obj=None):
        """Does the user have a specific permission?"""
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        """Does the user have permissions to view the app `app_label`?"""
        # Simplest possible answer: Yes, always
        return True
