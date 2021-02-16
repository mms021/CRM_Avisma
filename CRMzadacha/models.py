from django.db import models
from CRMmain.models import CRM_Lid_Zapros
from django.contrib.auth.models import User
from CRMcontacts.models import CRM_Contacts
import datetime

from CRMzakaz.models import CRM_Zakaz

SHOIS_PRIOR = [
    ('lo','Низкий'),
    ('mi','Средний'),
    ('hi','Высокий'),
]
PRIOR_ZAD = [
    ('nn','Не начат'),
    ('vr','В работе'),
    ('vi','Выполнено'),
    ('nv','Не выполнено'),
]

# Create your models here.
class CRM_Zadatha(models.Model):
    title = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        default='Запрос '
    )
    
    chec = models.CharField(
        max_length=50,
        choices=PRIOR_ZAD, 
        blank=True,
        null=True,
        default='vr'
    )

    zada = models.TextField(
        blank=True,
        null=True,
    )
    
    projects = models.ForeignKey(
        CRM_Lid_Zapros,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        
    )

    zakaz = models.ForeignKey(
        CRM_Zakaz,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,

    )
    prior = models.CharField(
        max_length=50,
        choices=SHOIS_PRIOR, 
        blank=True,
        null=True,
        default='mi'
    )

    srok = models.DateTimeField(
        max_length=50,
        blank=True,
        null=True,
        default=datetime.date.today() + datetime.timedelta(days=2,hours=12)
    )

    otvet = models.CharField(
        max_length=150,
        blank=True,
        null=True,
    )

    conact = models.ForeignKey(
        CRM_Contacts,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    created_by = models.CharField(
        "Автор",
        max_length=110,
        blank=True,
        null=True,
    )
    katigoria = models.CharField(
        'Категория',
        max_length=50,
        choices=[('za','Задача'),( 'pi','Письмо'),( 'zv','Звонок'),( 'vs','Встреча'),], 
        blank=True,
        null=True,
        default='za'
    )
    napominanie = models.BooleanField(
        'Ответственному',
        blank=True,
        null=True,
        default=False
    )
    napominanie_data = models.DateField(
        'Дата напоминания',
        max_length=50,
        blank=True,
        null=True,
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

    class Meta:
        ordering = ['-modified']