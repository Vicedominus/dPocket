from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from django.forms.widgets import EmailInput

from .models import User


class CustomUserAuthenticationForm(AuthenticationForm):
    """
    Authentication form for authenticating the user with email(USERNAME_FIELD) and password.
    """
    class Meta:
        model = User
        fields = ('username',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = EmailInput()
        self.fields['username'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['password'].widget.attrs.update({'class': 'form-control form-control-sm'})


class CustomUserCreationForm(UserCreationForm):
    """
    Create users with email and password with the UerCreationForm methods
    """
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control form-control-sm'})


class CustomUserPasswordResetForm(PasswordResetForm):
    """
    Reset the password of a user with the email
    """
    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-control form-control-sm'})


class CustomUserSetPasswordForm(SetPasswordForm):
    """
    Set a new password for the user
    """
    class Meta:
        model = User
        fields = ("email",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control form-control-sm'})

class CustomUserChangePasswordForm(PasswordChangeForm):
    """
    Change the user password
    """
    class Meta:
        model = User

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control form-control-sm'})