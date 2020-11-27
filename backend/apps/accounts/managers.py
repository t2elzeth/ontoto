from django.contrib.auth.models import BaseUserManager


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
