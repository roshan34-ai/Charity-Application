# Generated by Django 4.1.7 on 2023-04-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharityApp', '0008_rename_user_block_of_transactions_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='block_of_transactions',
            name='donation_for',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]