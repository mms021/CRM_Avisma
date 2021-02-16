from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail , send_mass_mail
from django.db.models import Q
from datetime import datetime , timedelta 
import openpyxl
import pytz
import calendar
from docxtpl import DocxTemplate 
from django.http import FileResponse
from django.conf.global_settings import MEDIA_ROOT
import os
from .models import CRM_Lid_Zapros , CRM_Product , CRM_Docs , CRM_Histori , CRM_Positions ,CRM_P_Postavka

from .forms import Lid_Zapros_Form , Docs_Form , Histori_Form ,Positio_Form , Lid_Zapros_Otkaz_Form

from CRMzadacha.forms import ZadathaForm , ZadathaFullForm  , ZadathaMinForm
from CRMzadacha.models import CRM_Zadatha 

from CRMzakaz.models import CRM_Zakaz
from CRMcontacts.models import CRM_Contacts
# Create your views here.

# Главна - Моя аналитика 
@login_required(login_url='/lg/')
def main(request):
   
    return render(request, 'CRMmain/prodject-myprod.html',{'projects':'proj','itap':'1'})

# Добавить продажу 
@login_required(login_url='/lg/')
def create(request):
    if request.method == 'POST':
        form = Lid_Zapros_Form( request.POST )
        if form.is_valid():
            form.save()
        return redirect('CRMmain:main')
    else:
        form = Lid_Zapros_Form()
    return render(request, 'CRMmain/prodject-create.html',{'form':form})


@login_required(login_url='/lg/')
def my_prod(request):
    lid = CRM_Lid_Zapros.objects.all()
    return render(request, 'CRMmain/prodject-myprod.html',{'lid':lid})



# Запрос
@login_required(login_url='/lg/')
def prodaja(request, pk):
    lid = CRM_Lid_Zapros.objects.get(id= pk) 
    zad = CRM_Zadatha.objects.filter(projects=lid)   # .exclude(chec='vi')
    doc = CRM_Docs.objects.filter(projects=lid)
    cont = CRM_Contacts.objects.filter(compani = lid.kompani)
    his = CRM_Histori.objects.filter(projects = lid)
    prod = CRM_Positions.objects.filter(projects = lid)
    f = {'1':'1. Проверка на складе','2':'2. Проверка квоты','3':'3. Проверка технологических возможностей','4':'1. Определение цены','5':'2. Определение периода производства', '6':'1. Формирование КП' ,'7':'2. Согласование КП','8':'3. Отправка КП клиенту'}
    try:
        zadchekk= CRM_Zadatha.objects.get(id= lid.prov_na_sklade)
    except :
        if lid.prov_na_nom < 9:
            zadchekk = CRM_Zadatha()
            zadchekk.projects = lid
            zadchekk.title = f[str(int(lid.prov_na_nom))]
            if str(int(lid.prov_na_nom)) == '3':
                zadchekk.user = User.objects.get(username='boss')
            else:
                zadchekk.user = request.user

            zadchekk.save()

            lid.prov_na_sklade = zadchekk.id
            lid.save()

   

    if request.method == 'POST':
        tip = request.POST.get('form')
        if tip == "form1":
            form1 = Lid_Zapros_Form( request.POST, instance=lid )
            if form1.is_valid():
                form1.save()
        #  Старые задачи
        elif tip == "form2":
            get = request.POST.get('idprog')
            form = ZadathaFullForm( request.POST, instance=CRM_Zadatha.objects.get(id= get) )
            if form.is_valid():
                c = form.save(commit=False)
                c.projects = lid
                c.save()


                if form.cleaned_data['chec'] =='vi' and form.cleaned_data['title'] == '3. Проверка технологических возможностей':
                    if lid.prov_na_nom < 9:
                        lid.prov_na_nom = lid.prov_na_nom + 1
                        lid.prov_na_sklade = None
                        lid.save()

        # Новая задача
        elif tip == "form3":
            form = ZadathaFullForm(request.POST)
            if form.is_valid():
                c = form.save(commit=False)
                c.projects = lid
                c.created_by = request.user.first_name
                c.save()
        # файлы
        elif tip == "form4":
            form = Docs_Form(request.POST , request.FILES)
            if form.is_valid():
                c = form.save(commit=False)
                c.projects = lid
                c.save()
        # История
        elif tip == "form5":
            form = Histori_Form(request.POST )
            if form.is_valid():
                c = form.save(commit=False)
                c.projects = lid
                c.save()

        # Новый продукт
        elif tip == "form6":
            form = Positio_Form(request.POST )
            if form.is_valid():
                c = form.save(commit=False)
                c.projects = lid
                spes = request.POST.getlist('spes')
                c.dop_k_splavy = ' '.join(spes)
                nad = round(sum([int(i)/100 for i in request.POST.getlist('nadb')] ),2)
                if nad == 0:   
                    c.proz_nadb = 1
                else:
                    c.proz_nadb = nad
                c.save()

                k = 0

                status = request.POST.getlist('status')
                ves = request.POST.getlist('ves')
                kol = request.POST.getlist('kol')
                data_sdad = request.POST.getlist('data_sdad')
                for i in request.POST.getlist('dataa'):
                    po = CRM_P_Postavka()
                    po.status = status[k]
                    po.data = i
                    po.data_sdad = data_sdad[k]
                    po.ves = ves[k]
                    po.kollitsh = kol[k]
                    po.posi = c
                    po.save()
                    k +=1 

        # Стаарый продукт 
        elif tip == "form6_old":
            get = CRM_Positions.objects.get(id=request.POST.get('ind')) 
            form = Positio_Form(request.POST , instance=get)
            if form.is_valid():
                c = form.save(commit=False)
                spes = request.POST.getlist('spes')
                c.dop_k_splavy = ' '.join(spes)

                nad = round(sum([int(i)/100 for i in request.POST.getlist('nadb')] ),2)
                print(nad)
                if nad == 0:   
                    c.proz_nadb = 1
                else:
                    c.proz_nadb = nad
                c.save()

            k = 0
            status = request.POST.getlist('status')
            ves = request.POST.getlist('ves')
            kol = request.POST.getlist('kol')
            data_sdad = request.POST.getlist('data_sdad')
            for i in request.POST.getlist('dataa'):
                po = CRM_P_Postavka()
                po.status = status[k]
                po.data = i
                po.data_sdad = data_sdad[k]
                po.ves = ves[k]
                po.kollitsh = kol[k]
                po.posi = c
                po.save()
                k +=1 

        elif tip == "formfor":   
            f = {'1':'1. Проверка на складе','2':'2. Проверка квоты','3':'3. Проверка технологических возможностей','4':'1. Определение цены','5':'2. Определение периода производства', '6':'1. Формирование КП' ,'7':'2. Согласование КП','8':'3. Отправка КП клиенту'}
            
            g = request.POST.get('idprog')
            form = ZadathaMinForm(request.POST , instance= zadchekk)
            if form.is_valid():
                c = form.save(commit=False)
                c.projects = lid
                c.title = f[g]
                c.created_by = request.user.first_name
                c.save()

                if form.cleaned_data['chec'] =='vi':
                    
                    if lid.prov_na_nom < 9:
                        lid.prov_na_nom = lid.prov_na_nom + 1
                        lid.prov_na_sklade = None
                        lid.save()
                        
        elif tip == 'form6_del_prod':
            get = request.POST.get('ind')
            f = CRM_Positions.objects.get(id=get)
            f.delete()

        elif tip == "form8":
            form1 = Lid_Zapros_Otkaz_Form( request.POST, instance=lid )
            if form1.is_valid():
                form1.save()

        elif tip == "formend":
            c = CRM_Zakaz()
            c.lid = lid
            c.title = f'Заказ {lid.title[6:]}' 
            c.kompani = lid.kompani
            c.users = lid.users
            c.save()

            lid.status = 'ZVR'
            lid.save()

        elif tip == 'docform':
            p = CRM_Positions.objects.get(id= request.POST.get('ind'))
            pos = CRM_P_Postavka.objects.filter(posi=p)
            
            prod = { 'SLIT':'Слитки','LIST':'Листы', 'ELIC':'Электроды', 'PLIT':'Плиты', 'LENT':'Лента', 'FOLG':'Фольга', 'PRYT':'Прутки', 'TRUB':'Трубы','PRIO':'Припой'}
            shi = {'1':'ASTM F 136','2':'ISO 5832-3','3':'BS 7252-3','4':'WS/D99/001', '5':'BMS-136','6':'DIN 65040'  }
            fp = [shi[i] for i in  p.dop_k_splavy.split(' ') ]
            doc4 = DocxTemplate("media/docshab.docx") 	
            context = {  
                'p':p , 
                'pp' : pos,
                 "koll": prod[p.izdelie] , 'f': ', '.join(fp) , 
                'datapol': '3' ,'dat': lid.created.strftime("%d.%m.%Y ")
            }
            doc4.render(context)
            doc4.save("media/dog.docx")

            #work = os.path.join(MEDIA_ROOT ,"dog.docx" )
            return FileResponse(open("media/dog.docx", 'rb'))
            

        return redirect(f'/kk/{pk}/')
    else:
        form1 = Lid_Zapros_Form(instance=lid)
        from3 = ZadathaFullForm()
        from4 = Docs_Form()
        from5 = Histori_Form()
        from6 = Positio_Form()
        from8 = Lid_Zapros_Otkaz_Form(instance=lid)

        if lid.prov_na_nom < 9:
            form7 = ZadathaMinForm(instance= zadchekk , initial={ 'user':User.objects.get(username='boss') })
        else:
            form7= None
    return render(request, 'CRMmain/prodject-box.html',{'lid':lid,'from8':from8,'form7':form7,'prod':prod,'form1':form1, 'form6':from6, 'form3':from3, 'form4':from4 , 'doc':doc ,'cont':cont, 'zada':zad , 'his':his , 'form5':from5 })



# Выйти 
def logout_view(request):
    success_url = reverse_lazy('CRMmain:logins')
    logout(request)
    return redirect(success_url)
# Войти 
def logins(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        try:
            if user is not None:
                login(request, user)
                return redirect('CRMmain:my_prod') # передалеть 
            else: 
                return redirect('CRMmain:logins')
        except:
            return redirect('CRMmain:logins') 
    return render(request, 'CRMmain/prodject-login.html' )
