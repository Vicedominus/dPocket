from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from .models import Movement, Account
from .forms import AccountForm, MovementForm, TransferForm

# ================== HOME RELATED VIEWS: ================== #
class HomeTemplateView(TemplateView):
    template_name = 'statement/home.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('statement')
        return super().get(*args, **kwargs)

# =================== END =========================== #

    
# =============== STATEMENT RELATED VIEWS: ==================== #
class StatementTemplateView(LoginRequiredMixin, TemplateView):

    template_name = 'statement/statement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['last_movements'] = Movement.objects.filter(user=self.request.user).order_by('-movement_date')[:10]
        context['accounts'] = Account.objects.filter(user=self.request.user)
        return context
# ===================== END =============================== #


# ===================== ACCOUNTS RELATED VIEWS: ======================= #
class AccountCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    
    model = Account
    form_class = AccountForm
    success_url = reverse_lazy('statement')
    template_name = 'statement/add_account.html'

    success_message = "A new account was created successfully"

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display accounts that belong to the authenticated user"""
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AccountListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    
    model = Account
    context_object_name = 'accounts'
    template_name = 'statement/list_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['accounts'] = Account.objects.filter(user=self.request.user)
        return context

class AccountUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Account
    form_class = AccountForm
    
    success_url = reverse_lazy('list_account')
    template_name = 'statement/edit_account.html'

    success_message = "The account was updated successfully"

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display accounts that belong to the authenticated user"""

        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AccountDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Account
    context_object_name = 'account'
    success_url = reverse_lazy('list_account')
    template_name = 'statement/delete_account.html'

    success_message = "The account was deleted successfully"
########################## END ############################


################ MOVEMENTS RELATED VIEWS: #######################
class MovementListView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    
    model = Movement
    context_object_name = 'movements'
    template_name = 'statement/list_movement.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['movements'] = Movement.objects.filter(user=self.request.user).order_by('-movement_date')
        return context


class MovementCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Movement
    form_class = MovementForm
    
    success_url = reverse_lazy('statement')
    template_name = 'statement/add_movement.html'

    success_message = "A new movement was added successfully"

    def get_form_kwargs(self):
        """ Pass the request object to the form class.
         This is necessary to only display accounts that belong to the authenticated user"""

        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        
        form.instance.user = self.request.user
        
        account = Account.objects.filter(account_name=form.instance.account).filter(user=self.request.user).first()
        if form.instance.movement_direction == 'OUT':
            account_new_value = account.account_amount - form.instance.movement_amount
            account.account_amount = account_new_value
            account.save()
        if form.instance.movement_direction == 'IN':
            account_new_value = account.account_amount + form.instance.movement_amount
            account.account_amount = account_new_value
            account.save()
        return super().form_valid(form)

class MovementUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Movement
    form_class = MovementForm
    
    success_url = reverse_lazy('list_movement')
    template_name = 'statement/edit_movement.html'

    success_message = "The movement was updated successfully"

    def get_object(self):
        return Movement.objects.get(id=self.kwargs['pk'])

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display accounts and categories that belong to the authenticated user"""

        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request        
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user

        """Step 1: Restore the account's amount previous the last movement
        If the last movement was an outcome add the movement's amount, if it 
        was an income substract the movemment amount from the account"""

        old_movement = Movement.objects.filter(id=self.object.pk).first()
        old_account = old_movement.account

        if old_movement.movement_direction == 'OUT':
            account_new_value = old_account.account_amount + old_movement.movement_amount
            old_account.account_amount=account_new_value
            old_account.save()
        if old_movement.movement_direction == 'IN':
            account_new_value = old_account.account_amount - old_movement.movement_amount
            old_account.account_amount=account_new_value
            old_account.save()

        """Step 2: Update the account with the new movement's amount provided in the form"""

        account = Account.objects.filter(account_name=form.instance.account).filter(user=self.request.user).first()
             
        if form.instance.movement_direction == 'OUT':
            account_new_value = account.account_amount - form.instance.movement_amount
            account.account_amount=account_new_value
            account.save()
        if form.instance.movement_direction == 'IN':
            account_new_value = account.account_amount + form.instance.movement_amount
            account.account_amount=account_new_value
            account.save()

        return super().form_valid(form)

class MovementDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Movement
    context_object_name = 'movement'
    success_url = reverse_lazy('list_movement')
    template_name = 'statement/delete_movement.html'

    success_message = "The movement was deleted successfully"

    def form_valid(self, form):

        """Wait a minute: Before delete, let's undone the changes made for the movement
        in the account when was created. If you make a mistake and you want to delete 
        the movement It is appropiate undone the changes in the model"""

        old_movement = Movement.objects.filter(id=self.object.pk).first()
        old_account = old_movement.account

        if old_movement.movement_direction == 'OUT':
            account_new_value = old_account.account_amount + old_movement.movement_amount
            old_account.account_amount=account_new_value
            old_account.save()
        if old_movement.movement_direction == 'IN':
            account_new_value = old_account.account_amount - old_movement.movement_amount
            old_account.account_amount=account_new_value
            old_account.save()

        return super().form_valid(form)
########################## END ############################


class TransferFormView(LoginRequiredMixin, FormView):
    login_url = reverse_lazy('login')

    form_class = TransferForm
    success_url = reverse_lazy('statement')
    template_name = 'statement/transfer.html'

    success_message = "A new transfer was created successfully"

    def get_form_kwargs(self):
        """ Pass the request object to the form class.
         This is necessary to only display accounts that belong to the authenticated user"""

        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        account_origin = Account.objects.filter(account_name=form.cleaned_data.get('account_origin')).first()
        account_end = Account.objects.filter(account_name=form.cleaned_data.get('account_end')).first()

        account_origin.account_amount = account_origin.account_amount - form.cleaned_data.get('amount_origin')
        account_end.account_amount = account_end.account_amount + form.cleaned_data.get('amount_end')

        account_origin.save()
        account_end.save()
        
        
        movement_out = Movement.objects.create(movement_direction='OUT', movement_amount=form.cleaned_data.get('amount_origin'), movement_description=form.cleaned_data.get('description'), movement_date=form.cleaned_data.get('transfer_date'), account=form.cleaned_data.get('account_origin'), user=self.request.user)
        movement_in = Movement.objects.create(movement_direction='IN', movement_amount=form.cleaned_data.get('amount_end'), movement_description=form.cleaned_data.get('description'), movement_date=form.cleaned_data.get('transfer_date'), account=form.cleaned_data.get('account_end'), user=self.request.user)
        
        movement_in.save()
        movement_out.save()

        return super().form_valid(form)