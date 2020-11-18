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

        self.prettify_validated_data()

        user = models.User.objects.create_user(
            password=password,
            **self.validated_data
        )
        return user

    def prettify_validated_data(self):
        """
        Filters the data in `validated_data`
        so that it can be passed to the `User` model
        """
        current_date = datetime.datetime.now()

        # Remove unnecessary data
        self.validated_data.pop('password')
        self.validated_data.pop('password2')

        # Add required, but not included in request data
        self.validated_data['last_login'] = current_date
        self.validated_data['date_joined'] = current_date
        return self.validated_data
