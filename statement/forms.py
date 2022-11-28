from django import forms
from .models import Category, Account, Movement, Currency
       

class MovementForm(forms.ModelForm):
    """
    A form representing the Movement model
    """
    class Meta:
        model = Movement

        fields = ('movement_date', 'movement_direction', 'account', 'category', 'movement_amount', 'movement_description', )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request') 
        super().__init__(*args, **kwargs)
        self.fields['movement_direction'].choices = Movement.MOVEMENT_DIRECTION
        self.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        self.fields['account'].queryset = Account.objects.filter(user=self.request.user)

        self.fields['movement_date'].widget.attrs.update({'class': 'form-control form-control-sm', 'placeholder':"MM/DD/YYYY"})
        self.fields['movement_direction'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['movement_amount'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['movement_description'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['category'].widget.attrs.update({'class': 'form-select form-select-sm'})
        self.fields['account'].widget.attrs.update({'class': 'form-select form-select-sm'})



class AccountForm(forms.ModelForm):
    """
    A form representing the Account model
    """
    class Meta:
        model = Account
        fields = ('account_name', 'account_amount', 'currency', )

    def __init__(self, *args, **kwargs):
        # User authenticated
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['currency'].queryset = Currency.objects.filter(user=self.request.user)

        self.fields['account_name'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['account_amount'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['currency'].widget.attrs.update({'class': 'form-control form-control-sm'})
        

class TransferForm(forms.Form):
    """
    A form for creating transfers
    """
    transfer_date = forms.DateField()
    account_origin = forms.ModelChoiceField(queryset=Account.objects.all())
    amount_origin = forms.DecimalField(max_digits=13, decimal_places=2)
    account_end = forms.ModelChoiceField(queryset=Account.objects.all())
    amount_end = forms.DecimalField(max_digits=13, decimal_places=2)
    description = forms.CharField(max_length=150, min_length=0)

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super().__init__(*args, **kwargs)
        self.fields['account_origin'].queryset = Account.objects.filter(user=self.request.user)
        self.fields['account_end'].queryset = Account.objects.filter(user=self.request.user)

        self.fields['account_origin'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['account_end'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['amount_origin'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['amount_end'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['transfer_date'].widget.attrs.update({'class': 'form-control form-control-sm'})
        self.fields['description'].widget.attrs.update({'class': 'form-control form-control-sm'})