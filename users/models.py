from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, AbstractBaseUser

from django.utils import timezone

# --------- User model with email as username field with a custom User Manager. -------- #

class CustomUserManager(BaseUserManager):
    """
    Custom UserManager to create the CustomUser objects
    """

    def create_user(self, email, password, **other_fields):
        """Create a user with email and password, normalize the email, set the password"""
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **other_fields):
        """Create a super user with create_user() but set superuser permissions"""
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(email, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User to work with instead of working directly on default User. The email is the username field.
    """
    email = models.EmailField(unique=True)
    start_date = models.DateTimeField(default=timezone.now)

    # These methods allow the admin to control access of the user to admin content
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)   # next i'm gonna set this to False and make the users activate theirs accounts via mail 

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


# Ref
# https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User
# https://docs.djangoproject.com/en/4.1/topics/auth/customizing/#custom-users-admin-full-example