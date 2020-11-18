import datetime

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
        style={
            'input_type': 'password'
        },
        write_only=True
    )

    class Meta:
        model = models.User
        fields = [
            'email',
            'phone',
            'password',
            'password2',
            'description'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {
                    'input_type': 'password'
                }
            }
        }

    def create(self, validated_data):
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        if password != password2:
            raise serializers.ValidationError({
                'password': "Passwords didn't match"
            })

        user = models.User.objects.create_user(
            email=validated_data.get('email'),
            password=password,
            phone=validated_data.get('phone'),
            description=validated_data.get('description'),
            last_login=datetime.datetime.now()
        )

        return user
