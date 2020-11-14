from django.contrib.auth.forms import UserCreationForm
from .models import Customer


class CustomerForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = (
            'username', 'first_name', 'last_name',
            'password1', 'password2', 'email', 'phone'
        )
