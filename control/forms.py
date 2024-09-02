from accounts.models import CustomUser
from django import forms

# Forms 
class AddUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
