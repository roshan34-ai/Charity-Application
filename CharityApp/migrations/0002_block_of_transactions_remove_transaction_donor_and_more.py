# Generated by Django 4.1.7 on 2023-03-29 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CharityApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block_Of_Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=7, max_digits=10)),
                ('from_account', models.CharField(max_length=100)),
                ('to_account', models.CharField(default='1234567891112', max_length=100)),
                ('message', models.CharField(blank=True, max_length=500, null=True)),
                ('hash', models.CharField(max_length=10)),
                ('prev_hash', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='donor',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('donor', 'donor')], max_length=50),
        ),
        migrations.DeleteModel(
            name='Requirement_Details_Model',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.AddField(
            model_name='block_of_transactions',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
