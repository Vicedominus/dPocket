from django.db import models
from django.conf import settings


# Create your models here.
class Currency(models.Model):
    currency_symbol = models.CharField(max_length=3, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.currency_symbol

class Category(models.Model):
    category_name = models.CharField(max_length=50, blank=False, null=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name

class Account(models.Model):
    account_name = models.CharField(max_length=100, blank=False, null=False)
    account_amount = models.DecimalField(blank=False, null=False, max_digits=13, decimal_places=2, default=0.00)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.account_name

class Movement(models.Model):
    MOVEMENT_DIRECTION = (
        ('IN', 'Income'),
        ('OUT', 'Outcome'),
    )
    movement_direction = models.CharField(max_length=3, choices=MOVEMENT_DIRECTION)
    movement_amount = models.DecimalField(blank=False, null=False, max_digits=13, decimal_places=2, default=0.00)
    movement_description = models.CharField(max_length=150, blank=True, null=True)
    movement_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.movement_direction+' , $ '+str(self.movement_amount)+', '+str(self.movement_description)+', '+str(self.movement_date)

