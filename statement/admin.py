from django.contrib import admin
from .models import Account, Category, Currency, Movement

# Register your models here.
admin.site.register(Account)
admin.site.register(Currency)
admin.site.register(Category)
admin.site.register(Movement)