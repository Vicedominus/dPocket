from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('statement/', StatementTemplateView.as_view(), name='statement'),
    
    path('statement/add_account/', AccountCreateView.as_view(), name='add_account'),
    path('statement/accounts/', AccountListView.as_view(), name='list_account'),
    path('statement/edit_account/<int:pk>/', AccountUpdateView.as_view(), name='edit_account'),
    path('statement/delete_account/<int:pk>/', AccountDeleteView.as_view(), name='delete_account'),

    path('statement/add_movement/', MovementCreateView.as_view(), name='add_movement'),
    path('statement/movements/', MovementListView.as_view(), name='list_movement'),
    path('statement/edit_movement/<int:pk>/', MovementUpdateView.as_view(), name='edit_movement'),
    path('statement/delete_movement/<int:pk>/', MovementDeleteView.as_view(), name='delete_movement'),

    path('statement/transfer/', TransferFormView.as_view(), name='transfer'),
]    