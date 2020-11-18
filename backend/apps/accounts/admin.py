from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ('is_staff',)
    list_display = (
        'email', 'confirmed',
        'is_active', 'is_superuser', 'is_staff'
    )
    list_filter = (
        'is_staff',
    )
    readonly_fields = (
        'id', 'date_joined', 'last_login'
    )

    fieldsets = (
        (None, {
            'fields': (
                'id',
                'email', 'phone', 'description',
                'last_login', 'date_joined',
                'confirmed',
                'is_active', 'is_superuser', 'is_staff',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)
