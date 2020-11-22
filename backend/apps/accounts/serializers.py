from rest_framework import serializers

from . import models


class UserDetailSerializer(serializers.ModelSerializer):
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
            'id',
            'full_name',
            'email',
            'phone',
            'password',
            'password2',
            'description'
        ]
        extra_kwargs = {
            'id': {
                'read_only': True
            },
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            },
        }

    def validate(self, data: dict):
        """Custom data validation"""
        password = data.get('password')
        password2 = data.get('password2')

        # Check if given passwords match
        if password != password2:
            raise serializers.ValidationError({
                'password': "Passwords didn't match"
            })

        # If everything is okay, just return given data
        return data

    def get_model(self):
        """Returns model specified in Meta class' `model` field"""
        return self.Meta.model

    def create(self, validated_data: dict):
        """Create user"""
        password = validated_data.get('password')

        model = self.get_model()
        user = model.objects.create_user(password, validated_data)
        return user
