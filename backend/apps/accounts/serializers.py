from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'id', 'email', 'phone', 'description'
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        required=True
    )

    class Meta:
        model = models.User
        fields = [
            'full_name',
            'email',
            'phone',
            'password',
            'password2',
            'description'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    def validate(self, data: dict):
        password = data.get('password')
        password2 = data.get('password2')

        if password != password2:
            raise serializers.ValidationError({
                'password': "Passwords didn't match"
            })
        return data

    def create(self, validated_data: dict):
        password = validated_data.get('password')

        prettified_data = self.prettify_validated_data(validated_data)

        user = models.User.objects.create_user(
            password=password,
            **prettified_data
        )
        return user

    @staticmethod
    def prettify_validated_data(data: dict):
        return models.User.prettify_data(data)
