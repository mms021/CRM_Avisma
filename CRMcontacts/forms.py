from .models import CRM_Contacts, CRM_Kompani
from django import forms

class ContactsForm(forms.ModelForm):
    class Meta:
        model = CRM_Contacts
        fields = ['title','doljnost', 'tel_nomber', "email", 'compani']
        labels = { 'title': ('ФИО'), 'doljnost': ('Должность') , 'tel_nomber' :('Телефон'),'email': ('Почта '),  "compani":('Контрагент ') }
        


class KompaniForm(forms.ModelForm):
    class Meta:
        model = CRM_Kompani
        fields = ['title','title_eng','tip','kod_WMS','kod_ERP','registr', 'sfera','saits','telefon' ,'email','opisanie' ,'contru', 'siti']
        labels = {'title':('Наименование'),'title_eng':('Наименование на англ.'),'tip':('Тип'),'kod_WMS':('Код WMS'),'contru':('Страна'),'siti':('Город'), 'kod_ERP':('Код ERP'),'registr':('Место государственной регистрации'), 'sfera':('Сфера деятельности'),'saits':('Сайт'),'telefon':('Телефон '), 'opisanie':('Описание') }
        


class ContactsFulForm(forms.ModelForm):
    class Meta:
        model = CRM_Contacts
        exclude = ('modified','created',)
        labels = { 'title': ('ФИО'), 'doljnost': ('Должность') , 'tel_nomber' :('Телефон'),'email': ('Почта '),  "compani":('Контрагент ') }
        




class KompaniFullForm(forms.ModelForm):
    class Meta:
        model = CRM_Kompani
        exclude = ('modified','created',)
        labels = {'title':('Наименование'),'title_eng':('Наименование на англ.'),'tip':('Тип'),'kod_WMS':('Код WMS'),'contru':('Страна'),'siti':('Город'), 'kod_ERP':('Код ERP'),'registr':('Место государственной регистрации'), 'sfera':('Сфера деятельности'),'saits':('Сайт'),'telefon':('Телефон '), 'opisanie':('Описание') }
        









