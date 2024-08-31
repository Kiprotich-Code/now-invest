from django.db import models
from django.utils import timezone
from accounts.models import CustomUser

# Models 
class Account(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='account')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
    # Automatically pull the account number from CustomUser
    account_no = models.CharField(max_length=12, editable=False, unique=True)

    def deposit(self, amount):
        """Deposits money to the user's account"""
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        """Withdraws money from the user's account, if sufficient balance exists"""
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.save()

    def __str__(self):
        return f"Account of {self.user.email}, Account No: {self.account_no}, Balance: {self.balance}"


# Transaction model (to log deposits and withdrawals)
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_type.capitalize()} of {self.amount} on {self.date}"