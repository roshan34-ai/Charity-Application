from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserModel(AbstractUser):
    username = models.CharField(
        max_length=50, 
        null=True, 
        blank=True
    )
    email = models.EmailField(
        _('email address'), 
        unique = True
    )
    name = models.CharField(
        max_length=50
    )
    phone_number = models.CharField(
        max_length=13
    )
    role = models.CharField(
        max_length=50, 
        choices = [('admin','admin'),('donor','donor')]
    )
    address = models.CharField(
        max_length=250, 
        null=True, 
        blank=True
    )
    password = models.CharField(
        max_length=15
    )
    is_varified = models.CharField(
        max_length=20, 
        default=False
    )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
      return "{}".format(self.email)
    

class Block_Of_Transactions(models.Model):
    user_id = models.ForeignKey(
        UserModel, 
        on_delete=models.CASCADE, 
        related_name="d_user"
    )
    donation_for = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    amount_paid = models.DecimalField(
        decimal_places=2, 
        max_digits=10
    )
    from_account = models.CharField(
        max_length=100
    )
    to_account = models.CharField(
        max_length=100,
        default="1234567891112131",
        null=True,
        blank=True
    )
    Adhar_number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    PAN_Number = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    message = models.CharField(
        max_length=500, 
        null=True, 
        blank=True
    )
    hash = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    prev_hash = models.CharField(
        max_length=10,
        null=True,
        blank=True
    )
    
    def __str__(self) -> str:
        return self.donor
    

    def create_hash(donor):
        data = UserModel.objects.get(id = donor)
        pass

    def get_prev_hash():
        pass
   