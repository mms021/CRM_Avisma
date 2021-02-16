from django.db import models
from CRMcontacts.models import CRM_Contacts , CRM_Kompani 
from CRMmain.models import CRM_Lid_Zapros
from django.contrib.auth.models import User
# Create your models here.

STATUS = [
    ('ACT','В работе'),
    ('RES','Приостановлен'),
    ('ZVR','Завершен'),
]

# Запрос ЛИД
class CRM_Zakaz(models.Model):
    # Название
    title = models.CharField(
        'Название',
        max_length=200,
        default='',
    )
    kompani = models.ForeignKey(
        CRM_Kompani,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    lid = models.ForeignKey(
        CRM_Lid_Zapros,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    users = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    opisanie = models.TextField(
        "Описание",
        max_length=200,
        blank=True,
        null=True,
        default='',
    )
    status= models.CharField(
        "Статус",
        max_length=10,
        choices=STATUS,
        blank=True,
        null=True,
        default='ACT'
    )
    
    postavshik = models.CharField(
        'Поставщик',
        max_length=100,
        blank=True,
        null=True,
        default=''
    )
    

    prov_na_sklade = models.CharField(
        max_length=10,
        blank=True,
        null=True,
    )
    prov_na_nom = models.FloatField(
        max_length=10,
        blank=True,
        null=True,
        default=1
    )

    objects = models.Manager()

    modified = models.DateTimeField(
        auto_now=True
    )
    created = models.DateTimeField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    def __str__(self):
        return self.title



