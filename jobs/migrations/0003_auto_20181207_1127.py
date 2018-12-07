# Generated by Django 2.1 on 2018-12-07 11:27

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0002_auto_20181207_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='contract',
            name='contract_created_by',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='contract',
            name='contract_expiry_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Contract Expiry Date'),
        ),
        migrations.AlterField(
            model_name='contract',
            name='date_created',
            field=models.DateField(default=datetime.date.today, verbose_name='Contract Start Date'),
        ),
    ]
