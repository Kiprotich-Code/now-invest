from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddUserForm, UpdateUserForm
from accounts.models import CustomUser
from django.views.generic import ListView , DeleteView, DetailView, UpdateView
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

def update_account(request, id):
    acc = Account.objects.get(id=id)  # Fetch the account object or return 404 if not found
    if request.method == 'POST':
        new_status = request.POST.get('status')  # Get the status from the button value
        if new_status:
            acc.status = new_status  # Update the account's status
            acc.save()  # Save the change to the database
            return redirect('accounts')  # Redirect to account detail page or another appropriate page
    
    return render(request, 'accounts/account_update.html', {'account': acc})


class AccountDeleteView(DeleteView):
    model = Account
    success_url = '/dashboad/accounts/'
    template_name = 'accounts/confirm_delete_account.html'


# TRANSACTION VIEWS
class TransactionListView(ListView):
    context_object_name = 'transactions'
    model = Transaction
    template_name = 'transactions/transactions.html'
    paginate_by = 10


def update_transaction(request, id):
    transaction = get_object_or_404(Transaction, id=id)

    # Prevent updates to rejected transactions
    if transaction.tr_status == 'Rejected':
        return render(request, 'transactions/transaction_update.html', {
            'transaction': transaction,
            'error_message': 'Rejected transactions cannot be modified.'
        })

    if request.method == 'POST':
        new_status = request.POST.get('tr_status')  # Get the status from the button value
        if new_status:
            transaction.tr_status = new_status
            transaction.save()  # Save the change to the database
            return redirect('transactions')  # Redirect to transaction list page or another appropriate page
    
    return render(request, 'transactions/transaction_update.html', {'transaction': transaction})


# ADMIN PROFILE 
def admin_profile(request):
    admin_info = CustomUser.objects.get(id=request.user.id)
    return render(request, 'admin_profile.html', {'admin_info': admin_info})