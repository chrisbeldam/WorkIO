# Generated by Django 2.1 on 2019-01-15 21:38

import datetime
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
            name='Contract',
            fields=[
                ('contract_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('contract_title', models.CharField(max_length=100)),
                ('contract_description', models.CharField(max_length=250)),
                ('contract_location', models.CharField(max_length=100)),
                ('contract_monthly_salary', models.IntegerField()),
                ('contract_recruiter', models.CharField(max_length=250)),
                ('recruiter_email', models.EmailField(max_length=254)),
                ('recruiter_telephone', models.CharField(max_length=11)),
                ('featured_contract', models.BooleanField(default=False)),
                ('featured_expiry_date', models.DateField(default=datetime.date.today)),
                ('date_created', models.DateField(default=datetime.date.today, verbose_name='Contract Start Date')),
                ('contract_expiry_date', models.DateField(default=datetime.date.today, verbose_name='Contract Expiry Date')),
                ('contract_created_by', models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
