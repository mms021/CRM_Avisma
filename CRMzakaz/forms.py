
from django import forms
from .models import  CRM_Zakaz

#from .models import CRM_Lid_Zapros ,  CRM_Docs , CRM_Histori , CRM_Positions

class Form_CRM_Zakaz(forms.ModelForm):
    class Meta:
        model = CRM_Zakaz
        exclude = ('modified','created','lid','prov_na_nom','prov_na_sklade','opisanie')
        labels = {  'kompani': ('Компания') , 'users': ('Менеджер')}
        







