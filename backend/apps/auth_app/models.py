from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Customer(AbstractUser):
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)
    is_verified = models.BooleanField(verbose_name='Подтвержден', default=False)
    phone = models.CharField(verbose_name='Номер телефона', max_length=20, blank=True, null=True)
    description = models.TextField(verbose_name='Описание профиля', blank=True, null=True)

    REQUIRED_FIELDS = (
        'username', 'first_name',
        'last_name', 'phone'
    )

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

    def get_username(self):
        return self.email
