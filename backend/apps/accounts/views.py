from rest_framework import generics

from rest_framework.exceptions import ValidationError

from . import serializers, models


class UserCreateView(generics.CreateAPIView):
    serializer_class = serializers.UserCreateSerializer
