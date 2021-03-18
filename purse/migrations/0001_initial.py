# Generated by Django 3.1.7 on 2021-03-17 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Wallet')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Balance')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='URL')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Owner')),
            ],
            options={
                'verbose_name': 'Wallet',
                'verbose_name_plural': 'Wallets',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=500, verbose_name='Comment')),
                ('summa', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Balance')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='purse.wallet', verbose_name='Wallet')),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
                'ordering': ['-created'],
            },
        ),
    ]
