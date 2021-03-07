from os import getenv

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

User = get_user_model()

USER_DEFAULT_USERNAMES = {"email": "admin@gmail.com", "username": "admin", "phone": "996312312312"}


class Command(BaseCommand):

    def handle(self, *args, **options):
        default_username = USER_DEFAULT_USERNAMES.get(User.USERNAME_FIELD)
        if default_username is None:
            raise ValueError("Unsupported `USERNAME_FIELD`")

        default_password = "admin"

        username = getenv("DJANGO_ADMIN_USERNAME") or default_username
        password = getenv("DJANGO_ADMIN_PASSWORD") or default_password

        user_filter = {User.USERNAME_FIELD: username}
        if not User.objects.filter(**user_filter).exists():
            print(f"{username} user has been created!")
            User.objects.create_superuser(username, password)
