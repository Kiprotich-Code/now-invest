from django.shortcuts import render, redirectn 
from .forms import AddUserForm

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
            return redirect