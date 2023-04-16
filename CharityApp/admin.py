from django.contrib import admin
from .models import UserModel, Block_Of_Transactions

# Register your models here.

@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
        list_display = ['id', 'username', 'email', 'name', 'phone_number', 'role', 'address', 'password', 'is_varified']

@admin.register(Block_Of_Transactions)
class Block_Of_Transactions(admin.ModelAdmin):
        list_display = ['id', 'user_id', 'donation_for', 'amount_paid', 'from_account', 'to_account', 'Adhar_number', 'PAN_Number', 'message', 'hash', 'prev_hash']