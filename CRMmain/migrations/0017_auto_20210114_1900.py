# Generated by Django 3.0.4 on 2021-01-14 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMmain', '0016_auto_20210114_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm_p_postavka',
            name='data',
            field=models.DateField(blank=True, max_length=100, null=True),
        ),
    ]
