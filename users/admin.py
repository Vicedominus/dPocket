from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


class UserAdmin(BaseUserAdmin):
    """
    A custom UserAdmin to create and change users in the admin panel
    """
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_active', 'is_staff', 'start_date',)
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'start_date',)}),
        ('Permissions', {'fields': ('is_active','is_staff')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


# Now register the new UserAdmin...
admin.site.register(User, UserAdmin)


# Ref 
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-users-admin-full-example