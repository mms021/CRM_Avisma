from django import forms

from .models import CRM_Lid_Zapros ,  CRM_Docs , CRM_Histori , CRM_Positions

class Lid_Zapros_Form(forms.ModelForm):
    class Meta:
        model = CRM_Lid_Zapros
        fields = ['title','kompani', 'contacts', "users",'postavshik','status']
        labels = { 'title': ('Название'), 'kompani': ('Компания') , 'contacts' :('Контакт'),'users': ('Менеджер'),'status':('Статус') }
        
class Lid_Zapros_Otkaz_Form(forms.ModelForm):
    class Meta:
        model = CRM_Lid_Zapros
        fields = ['otkaz_tip', 'otkaz_prith']
        widgets = {
            'otkaz_prith': forms.Textarea(attrs={'cols': 5, 'rows': 5}),
        }




class Docs_Form(forms.ModelForm):
    class Meta:
        model = CRM_Docs
        fields = ['title','opisanie', 'filefild']
        labels = { 'title': ('Название'), 'opisanie': ('Описание') ,'filefild':('Файл') }
        


class Histori_Form(forms.ModelForm):
    class Meta:
        model = CRM_Histori
        fields = ['title','komentrp' ]
        labels = { 'title': ('Тема'),"komentrp":('Описание')  }
        

class Positio_Form(forms.ModelForm):
    class Meta:
        model = CRM_Positions
        exclude = ('modified','created','projects',)
       
        







