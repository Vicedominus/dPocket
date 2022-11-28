from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *


urlpatterns = [
    path('login/', AuthLoginView.as_view(), name='login'),

    # The built-in LogoutView without override
    path('logout/', LogoutView.as_view(), name='logout'),

    path('signup/', RegistrationFormView.as_view(), name='signup'),

    path('change_password/', AuthPasswordChangeView.as_view(), name='change_password'),
    path('change_password_success/', AuthPasswordChangeDoneView.as_view(), name='change_password_successfully'),

    path('reset_password/', AuthPasswordResetView.as_view(), name='reset_password'),
    path('reset_password_done/', AuthPasswordResetDoneView.as_view(), name='reset_password_done'),
    path('reset_password_confirm/<uidb64>/<token>/', AuthPasswordResetConfirmView.as_view(), name='reset_password_confirm'),
    path('reset_password_complete/', AuthPasswordResetCompleteView.as_view(), name='reset_password_complete'),


]