from django.shortcuts import render
from accounts.models import CustomUser
from .models import Account

# Create your views here.
def home(request):
    return render(request, 'index.html')

def user_home(request):
    return render(request, 'user_home.html')


# ACCOUNTS VIEWS 
def acc_details(request):
    acc = Account.objects.get(user=request.user)

    context = {
        'acc': acc
    }

    return render(request, 'accounts/acc_details.html', context)