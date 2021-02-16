from django import template
from django.template.defaultfilters import stringfilter
from django.db.models import Q
import datetime 
from CRMzadacha.forms import ZadathaForm , ZadathaFullForm
from CRMzadacha.models import CRM_Zadatha

from  CRMcontacts.models import CRM_Contacts , CRM_Kompani
from CRMmain.models import CRM_Lid_Zapros , CRM_Docs
from CRMzakaz.models import CRM_Zakaz

register = template.Library()

#Все LID запросы
@register.filter(name='vselidy')
def vselidy(value):
    try:
        return CRM_Lid_Zapros.objects.filter(kompani__id=value)
    except:
        return None

#Все заказы
@register.filter(name='vszakazy')
def vszakazy(value):
    try:
        return CRM_Zakaz.objects.filter(kompani__id=value)
    except:
        return None




@register.filter(name='kollid')
def kollid(value):
    return CRM_Lid_Zapros.objects.filter(kompani__id=value).count()
    

#Все LID запросы колличество 
@register.filter(name='vselidyCount')
def vselidyCount(value):
    try:
        return CRM_Lid_Zapros.objects.filter(kompani__id=value).count()
    except:
        return 0 

# Колличество сотрудников 
@register.filter(name='countcotrud')
def countcotrud(value):
    try:
        return CRM_Contacts.objects.filter(compani__id=value).count()
    except:
        return 0 

# Колличество ЗАДАЧ
@register.filter(name='zadathacount')
def zadathacount(value):
    try:
        return CRM_Zadatha.objects.filter(projects__kompani__id=value).exclude(chec='vi').count()
    except:
        return 0 

# Колличество DOC
@register.filter(name='doccount')
def doccount(value):
    try:
        return CRM_Docs.objects.filter(projects__kompani__id=value).count()
    except:
        return 0 

#  ЗАДАЧИ
@register.filter(name='zada')
def zada(value):
    try:
        return CRM_Zadatha.objects.filter(projects__kompani__id=value).exclude(chec='vi')
    except:
        return 0 

