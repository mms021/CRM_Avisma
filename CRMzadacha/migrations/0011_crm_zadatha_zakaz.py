# Generated by Django 3.0.4 on 2021-01-15 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRMzakaz', '0002_auto_20210115_1612'),
        ('CRMzadacha', '0010_auto_20210115_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='crm_zadatha',
            name='zakaz',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRMzakaz.CRM_Zakaz'),
        ),
    ]