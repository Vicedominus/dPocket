
# dPocket

dPocket is a web application that allows users to track their expenses, incomes, and bank accounts. Users can create an account by providing an email and password. Once a user logs in successfully, it can create categories, currencies, accounts, and movements(including incomes, outcomes, and transfers).

Additionally, users can change or reset their password via email.

## Working with Django

This project was intended to practice the basic concepts of the Django web framework. Many functionalities can be added as charts, downloading the statement as a spreadsheet, third-party API integration, and so on. Also, the database design and the UI/UX can be improved. All these elements and many others will be taken into account, if this project goes to production in the future.

The authentication system was built with a User model that extends the built-in AbstractBaseUser and by extending the built-in forms: AuthenticationForm, SetPasswordForm, PasswordChangeForm, AdminPasswordChangeForm, PasswordResetForm, UserCreationForm, UserChangeForm.
ref. (https://docs.djangoproject.com/en/4.1/topics/auth/customizing/)

The CRUDs functionalities were implemented with class-based views that extend the FormView, CreateView, UpdateView, and DeleteView. 
ref. (https://docs.djangoproject.com/en/4.1/ref/class-based-views/)


In most cases, the forms extend the built-in forms ModelForm with some changes in the fields.
ref. (https://docs.djangoproject.com/en/4.1/topics/forms/modelforms/#django.forms.ModelForm)

The LoginRequiredMixin was used to limit access to logged-in users, and the SuccessMessageMixin to add messages to the views.
ref. (https://docs.djangoproject.com/en/4.1/topics/auth/default/#django.contrib.auth.mixins.LoginRequiredMixin)
ref. (https://docs.djangoproject.com/en/4.1/ref/contrib/messages/)

In addition, the Django templates language was used to generate content dynamically and the Bootstrap framework to style the HTML via CDN.
ref. (https://docs.djangoproject.com/en/4.1/topics/templates/#the-django-template-language)
ref. (https://getbootstrap.com/docs/5.2/getting-started/introduction/)

### Conclusion

Django provides many built-in classes that make things easier and help us to save time in development. It's true that to be able to use it it's required a bit of OOP, but there are a lot of rewards if you can learn it. 