# Generated by Django 4.1.7 on 2023-03-29 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CharityApp', '0003_block_of_transactions_pan_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='block_of_transactions',
            name='Adhar_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
