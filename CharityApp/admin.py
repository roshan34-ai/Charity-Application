from django.contrib import admin
from .models import UserModel

# Register your models here.

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
        list_display = ['username', 'email', 'name', 'phone_number', 'role', 'address', 'password', 'is_varified']

