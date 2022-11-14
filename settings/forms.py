from django import forms

from statement.models import Category, Currency


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('category_name', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_name'].widget.attrs.update({'class': 'form-control form-control-sm'})


class CurrencyForm(forms.ModelForm):
    class Meta:
        model = Currency
        fields = ('currency_symbol', )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['currency_symbol'].widget.attrs.update({'class': 'form-control form-control-sm'})