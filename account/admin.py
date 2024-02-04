from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "username", "mobile")
    fields = (
                 "email", "username", "mobile",
                 "password", "first_name", "last_name","image","groups",
                 "user_permissions", "is_superuser", "is_staff", 
                 "is_active", "date_joined","last_login", 'is_private_account'
             )

