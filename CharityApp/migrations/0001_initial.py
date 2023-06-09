# Generated by Django 4.1.7 on 2023-03-29 16:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=13)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('needy', 'needy'), ('donor', 'donor')], max_length=50)),
                ('address', models.CharField(blank=True, max_length=250, null=True)),
                ('password', models.CharField(max_length=15)),
                ('is_varified', models.CharField(default=False, max_length=20)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_paid', models.DecimalField(decimal_places=7, max_digits=10)),
                ('acc_no', models.IntegerField()),
                ('message', models.CharField(blank=True, max_length=50, null=True)),
                ('hash', models.CharField(max_length=10)),
                ('prev_hash', models.CharField(max_length=10)),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='d_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Requirement_Details_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=50)),
                ('m_name', models.CharField(max_length=50)),
                ('l_name', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=50)),
                ('annual_income', models.DecimalField(blank=True, decimal_places=7, max_digits=7, null=True)),
                ('phone_number', models.CharField(max_length=13)),
                ('bank_account_number', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=50)),
                ('pan_number', models.CharField(blank=True, max_length=50, null=True)),
                ('adhar_numner', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=100)),
                ('approved', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
