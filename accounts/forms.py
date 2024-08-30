# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

# Step 1: Personal Information Form
class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'date_of_birth', 'phone_no', 'address']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'style': 'max-width: 400px', 'placeholder': "Date Of Birth"}),
            'first_name': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 400px', 'placeholder': "Official First Name"}),
            'last_name': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 400px', 'placeholder': "Official Last Name"}),
            'phone_no': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 400px', 'placeholder': "Phone No: i.e +254700234200"}),
            'address': forms.TextInput(attrs={'class': 'form-control',  'style': 'max-width: 400px', 'placeholder': "Address"}),
        }


# Step 2: Email & Password Form
class AccountInfoForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ['email', 'password1', 'password2']


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder' :'Email', 'style': 'max-width: 600px;'}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Password',
                'style': 'max-width: 600px;'
            }
        )
    )
