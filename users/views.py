from django.urls import reverse_lazy
from django.shortcuts import redirect, render

from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView
from django.views.generic.edit import FormView
from .forms import CustomUserAuthenticationForm, CustomUserCreationForm, CustomUserPasswordResetForm, CustomUserSetPasswordForm, CustomUserChangePasswordForm 


# -------------- SIGNUP RELATED VIEWS ---------------- #

class RegistrationFormView(FormView, SuccessMessageMixin):
    """
    A view for user creation with a form 
    """
    template_name = 'users/signup.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    success_message = "User created successfully. You can log in now." 

    def form_valid(self, form):
        """After successful submission: save the user and send a message"""
        # save the user
        user = form.save()
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if user is not None:
            if success_message:
                #send a message
                messages.success(self.request, success_message)
            return response
        return super().form_valid(form)

    def get(self, *args, **kwargs):
        """An authenticated user must be redirected if he tries to go to the signup page"""
        if self.request.user.is_authenticated:
            return redirect('statement')
        return super().get(*args, **kwargs)

# --------------------- END ------------------------------- #


# ----------------- LOGIN RELATED VIEWS -------------------- #

class AuthLoginView(LoginView, SuccessMessageMixin):
    """
    A view for user authentication with a form
    """
    template_name = 'users/login.html'
    next_page = reverse_lazy('statement')
    redirect_authenticated_user = True
    authentication_form = CustomUserAuthenticationForm

    success_message = "The login was successful. Welcome back." 

    def form_valid(self, form):
        """After successful submission, authenticate the user and send a message"""
        response = super().form_valid(form)
        success_message = self.get_success_message(form.cleaned_data)
        if success_message:
            # send a message
            messages.success(self.request, success_message)
            return response
        return super().form_valid(form)


# -------------------------- END ------------------------------ #


# --------------- PASSWORD RESET RELATED VIEWS --------------- #

class AuthPasswordResetView(PasswordResetView):
    """
    A view for resetting the user's password in case of forgetting it
    """
    template_name = 'users/reset_password.html'
    success_url = reverse_lazy('reset_password_done')
    subject_template_name = 'users/reset_password_subject.txt'
    email_template_name = 'users/reset_password_email.html'

    form_class = CustomUserPasswordResetForm


class AuthPasswordResetDoneView(PasswordResetDoneView):
    """
    A view for telling the user to check his email
    """
    template_name = 'users/reset_password_done.html'

class AuthPasswordResetConfirmView(PasswordResetConfirmView):
    """
    A view for setting a new password
    """
    template_name = 'users/reset_password_confirm.html'
    success_url = reverse_lazy('reset_password_complete')

    form_class = CustomUserSetPasswordForm

class AuthPasswordResetCompleteView(PasswordResetCompleteView):
    """
    Reset complete
    """
    template_name = 'users/reset_password_complete.html'

# -------------------- END -------------------------- #

# ----------------- PASSWORD CHANGE RELATED VIEWS ------------------ #

class AuthPasswordChangeView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView):
    """
    A view for changing the password of an authenticated user
    """
    template_name = 'users/change_password.html'
    success_url = reverse_lazy('settings')

    success_message = "Password successfully changed"

    form_class = CustomUserChangePasswordForm

class AuthPasswordChangeDoneView(LoginRequiredMixin, SuccessMessageMixin, PasswordChangeDoneView):
    """A view for sending a message after changing the password successfully"""

    success_message = "Password successfully changed"

# ---------------- END -------------------- #