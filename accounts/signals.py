from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import CustomUser
import uuid

# Receiver 
@receiver(post_save, sender=CustomUser)
def create_account_no(sender, instance, created, **kwargs):
    if created and not instance.account_no:
        # Generate a unique 12-character account number
        account_no = str(uuid.uuid4().int)[:12]  # First 12 digits from a UUID
        instance.account_no = account_no
        instance.save()
