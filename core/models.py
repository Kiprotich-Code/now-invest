from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Account model (to hold user's funds)
class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    
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
        return f"Account of {self.user.username}, Balance: {self.balance}"

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