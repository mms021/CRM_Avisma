from .models import CRM_Zadatha 
from django import forms

class ZadathaForm(forms.ModelForm):
    class Meta:
        model = CRM_Zadatha
        fields = ['title','prior', "zada", 'chec','srok']
        labels = { 'prior': ('Приоритет') , 'title': ('Название ') ,'chec':('Статус'), 'zada':('Задача') ,'srok':('Срок')}
        widgets = {
            'zada': forms.Textarea(attrs={'cols': 10, 'rows': 10}),
        }
        
class ZadathaFullForm(forms.ModelForm):
    class Meta:
        model = CRM_Zadatha
        fields = ['title','prior', 'user', "zada", 'chec','srok', 'projects','napominanie' ,"napominanie_data" , 'katigoria','created_by']
        labels = { 'prior': ('Приоритет') , 'title': ('Название ') ,'chec':('Статус'), 'zada':('') ,'srok':('Завершение'), 'user':('Ответственный')}
        widgets = {
            'zada': forms.Textarea(attrs={'cols': 10, 'rows': 10}),
            'napominanie': forms.CheckboxInput(),
        }
        

class ZadathaMinForm(forms.ModelForm):
    class Meta:
        model = CRM_Zadatha
        fields = ['user','chec']
        labels = { 'chec':('Статус'),  'user':('Ответственный')}
     