from djoser.serializers import UserCreateSerializer, UserSerializer

from rest_framework import serializers

from . import models


class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = models.Customer
        fields = (
            'email', 'username', 'password', 'first_name', 'last_name', 'phone'
        )
