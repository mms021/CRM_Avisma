# Generated by Django 3.0.4 on 2021-01-14 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRMmain', '0017_auto_20210114_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='crm_lid_zapros',
            name='proz_nadb',
            field=models.FloatField(blank=True, default=1, max_length=10, null=True),
        ),
    ]
