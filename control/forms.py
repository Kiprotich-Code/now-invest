from accounts.models import CustomUser
from django import forms
from django.contrib.auth.forms import UserChangeForm

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