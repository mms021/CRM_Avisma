from django import template
from django.template.defaultfilters import stringfilter
from django.db.models import Q
import datetime 
from CRMzadacha.forms import ZadathaForm , ZadathaFullForm
from CRMzadacha.models import CRM_Zadatha

from  CRMcontacts.models import CRM_Contacts , CRM_Kompani
from CRMmain.models import CRM_Lid_Zapros , CRM_Docs , CRM_Positions
import datetime

register = template.Library()


@register.filter(name='filtercount')
def filtercount(value):
    return CRM_Lid_Zapros.objects.filter(status=value).count()
   
       
#('RES'|filtercount,'В работе'), ('RES'

@register.filter(name='countzadathamod')
def countzadathamod(value):
    f = list(  CRM_Lid_Zapros.objects.exclude(status='OTC').values_list('users__first_name', flat=True).order_by('id'))
    h = []
    datafil = datetime.datetime.today()
    for i in list(set(f)):
        h.append(CRM_Zadatha.objects.exclude(chec='vi').filter(projects__users__first_name=i).exclude(created__gt=datafil).count())
    return h


@register.filter(name='titleproj')
def titleproj(value):
    j = CRM_Lid_Zapros.objects.exclude(status='OTC').values_list('title', flat=True).order_by('id')
    return [f[:15] for f in j]
   
@register.filter(name='collofProd')
def collofProd(value):
    c = [CRM_Positions.objects.filter(projects=i).count() for i in CRM_Lid_Zapros.objects.exclude(status='OTC').order_by('id') ]
    c.append(0)
    return c
   


@register.filter(name='fioprcount')
def fioprcount(value):
    f = list(  CRM_Lid_Zapros.objects.exclude(status='OTC').values_list('users__first_name', flat=True).order_by('id'))
    return list(set(f))

@register.filter(name='countprodforFIO')
def countprodforFIO(value):
    y = CRM_Lid_Zapros.objects.exclude(status='OTC').values_list('users__first_name', flat=True).order_by('id')
    return [ CRM_Lid_Zapros.objects.filter(users__first_name = h).filter(status=value).count() for h in list(set(y))]


@register.filter(name='contitaps')
def contitaps(value):
    d = value.split(' ')
    f = [ int(i) for i in d] 
    return CRM_Lid_Zapros.objects.exclude(status='OTC').filter(prov_na_nom__in=f ).count()
     


@register.filter(name='contitapslid')
def contitapslid(value):
    d = value.split(' ')
    f = [ int(i) for i in d] 
    
    return CRM_Lid_Zapros.objects.exclude(status='OTC').filter(prov_na_nom__in=f )
     




#Все LID запросы
@register.filter(name='vselidy')
def vselidy(value):
    try:
        return CRM_Lid_Zapros.objects.filter(kompani__id=value)
    except:
        return None

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

