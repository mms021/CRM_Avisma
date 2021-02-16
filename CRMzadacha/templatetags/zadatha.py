from django import template
from django.template.defaultfilters import stringfilter
from django.db.models import Q
import datetime 
from CRMzadacha.forms import ZadathaForm , ZadathaFullForm , ZadathaMinForm
from CRMzadacha.models import CRM_Zadatha
from CRMmain.models import CRM_Lid_Zapros , CRM_Positions , CRM_P_Postavka
from CRMmain.forms import Positio_Form
from CRMzakaz.models import CRM_Zakaz
register = template.Library()


@register.filter(name='postavkafilter')
def postavkafilter(value):
    return CRM_P_Postavka.objects.filter(posi_id=value)


@register.filter(name='datalastpostavki')
def datalastpostavki(value):
    try:
        #CRM_P_Postavka.objects.all().delete()
        return CRM_P_Postavka.objects.filter(posi__id=value).first().data
    except :
        return " "
    





@register.filter(name='formzad')
def formzad(value):
    return ZadathaFullForm(instance=CRM_Zadatha.objects.get(id = value))
    
@register.simple_tag
def form_tag(value):
    return ZadathaFullForm(instance=CRM_Zadatha.objects.get(id = value))
    
@register.simple_tag
def form_tag_full(value):
    return ZadathaFullForm(instance=CRM_Zadatha.objects.get(id = value))
    

#@register.simple_tag
# def form_tag_full_st1(value):
#     lid = CRM_Lid_Zapros.objects.get(id= value)
#     if lid.prov_na_sklade == None:
#         c = CRM_Zadatha(projects=lid)
#         c.title = 'Проверка на складе'
#         c.save()
#         lid.prov_na_sklade = c.id
#         lid.save()
#     else:
#         pass

#     return ZadathaFullForm(instance=CRM_Zadatha.objects.get(id = lid.prov_na_sklade))
    

@register.filter(name='shek')
def shek(value):
    return CRM_Lid_Zapros.objects.get(id = value).prov_na_sklade

@register.simple_tag
def form_tag_position(value):
    return Positio_Form(instance=CRM_Positions.objects.get(id = value))
    

@register.filter(name='mainpage')
def mainpage(value):
    return CRM_Zadatha.objects.exclude(chec='vi').filter(user=value)


@register.filter(name='mainpagecount')
def mainpagecount(value):
    return CRM_Zadatha.objects.exclude(chec='vi').filter(user=value).count()

@register.filter(name='myLid')
def myLid(value):
    return CRM_Lid_Zapros.objects.exclude(status='OTC').exclude(status='ZVR').filter(users=value).count()

@register.filter(name='myZakaz')
def myZakaz(value):
    return CRM_Zakaz.objects.filter(users=value).count()


@register.filter(name='filtpsitons')
def filtpsitons(value):
    try:
        return CRM_Positions.objects.filter(projects__id= value.projects.id)
    except :
        return None


@register.simple_tag
def chec_zad(value):
    return ZadathaMinForm(instance=CRM_Zadatha.objects.get(id = value) )
    

@register.filter(name='fullprise')
def fullprise(value):
    p =  CRM_Positions.objects.filter(projects__id= value)
    d = []
    for j in p:
        if j.kollitsh_kg != None:
            if j.proz_nadb == 1:
                d.append(j.proz_nadb )
            else:
                d.append( ((j.kollitsh_kg * j.proz_nadb) + j.kollitsh_kg ) )

        else:
            pass

    return  round( sum( d) * 25.40 , 2)

@register.filter(name='dolar')
def dolar(value):
    try:
        c = CRM_Positions.objects.get(id= value)
        if c.proz_nadb == 1:
            m = 0
        else:
            m= c.proz_nadb 
        return round(((c.kollitsh_kg * m) + c.kollitsh_kg ) *25.40  , 2) 
    except :
        return ''


@register.filter(name='пgetalldatapostavki')
def пgetalldatapostavki(value):
    return CRM_P_Postavka.objects.filter(posi__projects_id=value).order_by('data')




@register.filter(name='datatimefilss')
def datatimefilss(value):
    #print(value , datetime.datetime.now(datetime.timezone.utc))
    if datetime.datetime.now(datetime.timezone.utc) > value :
        return 'background: #ffdddd; '
    else:
        return ' '





@register.filter(name='checcount')
def checcount(value):
    datafil = datetime.datetime.today()
    return CRM_Zadatha.objects.exclude(chec='vi').filter(projects_id=value).exclude(srok__gt=datafil).count()

