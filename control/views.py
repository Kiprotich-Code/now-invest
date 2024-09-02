from django.shortcuts import render, redirect
from .forms import AddUserForm, UpdateUserForm
from accounts.models import CustomUser
from django.views.generic import CreateView, UpdateView, ListView , DeleteView
from core.models import Account, Transaction

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

# List View 
def ctrl_users(request):
    users = CustomUser.objects.all()
    return render(request, 'users/ctrl_users.html', {'users': users})

# Detail View 
def update_user(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_details')
        
    else:
        form = UpdateUserForm(instance=user)
    return render(request, 'users/update_user.html', {'form': form})


def user_details(request, user_id):
    user = CustomUser.objects.get(id=user_id)
    return render(request, 'users/user_details.html', {'user': user})


# CRUD ON ACCOUNTS
class AccountListView(ListView):
    context_object_name = 'accounts'
    model = Account
    template_name = 'accounts/accounts.html'
    paginate_by = 5

class AccountUpdateView(UpdateView):
    template_name = 'accounts/account_update.html'
    model = Account
    fields = ('title', 'sub_title', 'desc', 'category', 'author', )
    success_url = '/dashboard/accounts/'


class AccountDeleteView(DeleteView):
    model = Account
    success_url = '/dashboadr/accounts/'
    template_name = 'accounts/confirm_delete_account.html'

