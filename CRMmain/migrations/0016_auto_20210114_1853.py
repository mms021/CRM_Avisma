# Generated by Django 3.0.4 on 2021-01-14 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMmain', '0015_auto_20210114_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crm_p_postavka',
            name='data',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='crm_p_postavka',
            name='status',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Статус'),
        ),
    ]