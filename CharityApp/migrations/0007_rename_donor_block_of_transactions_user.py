# Generated by Django 4.1.7 on 2023-03-29 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CharityApp', '0006_alter_block_of_transactions_amount_paid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block_of_transactions',
            old_name='donor',
            new_name='user',
        ),
    ]