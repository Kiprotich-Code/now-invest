from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _
from .models import CustomUser

# Register the custom CustomUser model with the UserAdmin class
admin.site.register(CustomUser)