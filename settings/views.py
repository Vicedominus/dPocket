from django.urls import reverse_lazy
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from statement.models import Category, Currency
from .forms import CategoryForm, CurrencyForm

# ---------------- SETTINGS RELATED VIEWS: ---------------------- #
class SettingsTemplateView(LoginRequiredMixin, TemplateView):
    """
    A view for rendering the user's settings
    """
    template_name = 'settings/settings.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.filter(user=self.request.user)
        context['currencies'] = Currency.objects.filter(user=self.request.user)
        return context

# ---------------------- END -------------------------- #


# ---------------- CAREGORIES RELATED VIEWS: ---------------------- #
class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A view for creating a new category with a form
    """
    login_url = reverse_lazy('login')
    
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('settings')
    template_name = 'settings/add_category.html'

    success_message = "A new category was added successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    A view for updating categories with a form
    """
    login_url = reverse_lazy('login')
    model = Category
    form_class = CategoryForm
    
    success_url = reverse_lazy('settings')
    template_name = 'settings/edit_category.html'

    success_message = "The category was updated successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    A view for deleting a category
    """
    login_url = reverse_lazy('login')
    model = Category
    context_object_name = 'category'
    success_url = reverse_lazy('settings')
    template_name = 'settings/delete_category.html'

    success_message = "The category was deleted successfully"

# ----------------- END  -------------------------- #


#  ----------- CURENCIES RELATED VIEWS: -------------------- #
class CurrencyCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    """
    A view for creating a new currency with a form
    """
    login_url = reverse_lazy('login')
    
    model = Currency
    form_class = CurrencyForm
    success_url = reverse_lazy('settings')
    template_name = 'settings/add_currency.html'

    success_message = "A new currency was added successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CurrencyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """
    A view for updating currencies with a form
    """
    login_url = reverse_lazy('login')
    model = Currency
    form_class = CurrencyForm
    
    success_url = reverse_lazy('settings')
    template_name = 'settings/edit_currency.html'

    success_message = "The currency was updated successfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class CurrencyDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    """
    A view for deleting a currency
    """
    login_url = reverse_lazy('login')
    model = Currency
    context_object_name = 'currency'
    success_url = reverse_lazy('settings')
    template_name = 'settings/delete_currency.html'

    success_message = "The currency was deleted successfully"

# -------------------- END --------------------------- #
