from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ('is_staff',)

    list_display = (
        'email', 'is_confirmed',
        'is_active', 'is_superuser', 'is_staff'
    )

    list_filter = (
        'is_staff',
    )

    readonly_fields = (
        'id',
        'date_joined',
    )

    fieldsets = (
        (None, {
            'fields': (
                'id',
                'email', 'phone', 'description',
                'date_joined',
                'is_confirmed',
                'is_active', 'is_superuser', 'is_staff',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)

admin.site.unregister(Group)
