from django.shortcuts import render, redirect
from .forms import AddUserForm
from accounts.models import CustomUser

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

# CRUD ON USERS 
# CREATE - USER 
def add_user(request):
    if request.method == 'POST':
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ctrl_users')
        
    else: 
        form = AddUserForm()

    return render(request, 'users/add_user.html', {'form': form})

def ctrl_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users/ctrl_users.html', {'users': users})