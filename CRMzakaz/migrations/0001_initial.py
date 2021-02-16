# Generated by Django 3.0.4 on 2021-01-15 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CRMcontacts', '0008_crm_kompani_adress'),
        ('CRMmain', '0019_auto_20210114_1932'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CRM_Zakaz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200)),
                ('opisanie', models.TextField(blank=True, default='', max_length=200, null=True)),
                ('status', models.CharField(blank=True, choices=[('ACT', 'В работе'), ('RES', 'Приостановлен'), ('ZVR', 'Завершен')], default='ACT', max_length=10, null=True)),
                ('postavshik', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Поставщик')),
                ('prov_na_sklade', models.CharField(blank=True, max_length=10, null=True)),
                ('prov_na_nom', models.FloatField(blank=True, default=1, max_length=10, null=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('kompani', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRMcontacts.CRM_Kompani')),
                ('lid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CRMmain.CRM_Lid_Zapros')),
                ('users', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
