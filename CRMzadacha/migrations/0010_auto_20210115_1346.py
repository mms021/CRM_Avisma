# Generated by Django 3.0.4 on 2021-01-15 10:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMzadacha', '0009_auto_20210114_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm_zadatha',
            name='srok',
            field=models.DateTimeField(blank=True, default=datetime.date(2021, 1, 16), max_length=50, null=True),
        ),
    ]