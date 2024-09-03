from accounts.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserChangeForm
from core.models import Account

# Forms 
class AddUserForm(forms.ModelForm):
    class Meta:
        model  = CustomUser
        fields = ['first_name', 'last_name', 'phone_no', 'email', 'password', ]


class UpdateUserForm(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'phone_no', 'email', ]


class UpdateAccountStatusForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['status']