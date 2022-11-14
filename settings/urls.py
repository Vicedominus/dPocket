from django.urls import path
from .views import *

urlpatterns = [
    path('', SettingsTemplateView.as_view(), name='settings'),

    path('add_category', CategoryCreateView.as_view(), name='add_category'),
    path('edit_category/<int:pk>/', CategoryUpdateView.as_view(), name='edit_category'),
    path('delete_category/<int:pk>/', CategoryDeleteView.as_view(), name='delete_category'),

    path('add_currency', CurrencyCreateView.as_view(), name='add_currency'),
    path('edit_currency/<int:pk>/', CurrencyUpdateView.as_view(), name='edit_currency'),
    path('delete_currency/<int:pk>/', CurrencyDeleteView.as_view(), name='delete_currency'),
]