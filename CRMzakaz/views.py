from django.shortcuts import render

# Create your views here.
from .models import  CRM_Zakaz

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User

from .forms import Form_CRM_Zakaz

from CRMmain.forms import Lid_Zapros_Form , Docs_Form , Histori_Form ,Positio_Form , Lid_Zapros_Otkaz_Form
from CRMmain.models import CRM_Lid_Zapros , CRM_Product , CRM_Docs , CRM_Histori , CRM_Positions ,CRM_P_Postavka
from CRMzadacha.forms import ZadathaForm , ZadathaFullForm  , ZadathaMinForm
from CRMzadacha.models import CRM_Zadatha 

from CRMcontacts.models import CRM_Contacts , CRM_Kompani 



@login_required(login_url='/lg/')
def main(request):
    lid = CRM_Zakaz.objects.all() 
    return render(request, 'CRMzakaz/prodject-myprod.html',{'lid':lid })

@login_required(login_url='/lg/')
def zakaz(request, pk):
    lid = CRM_Zakaz.objects.get(id= pk) 
    zad = CRM_Zadatha.objects.filter(zakaz=lid)   # .exclude(chec='vi')
    #doc = CRM_Docs.objects.filter(projects=lid.projects)
    cont = CRM_Contacts.objects.filter(compani = lid.kompani)
    #his = CRM_Histori.objects.filter(projects = lid.projects)
    prod = CRM_Positions.objects.filter(projects = lid.lid.id)

    if request.method == 'POST': 
        tip = request.POST.get('form')
        if tip == "form1":
                form1 = Form_CRM_Zakaz( request.POST, instance=lid )
                if form1.is_valid():
                    form1.save()

        #  Старые задачи
        elif tip == "form2":
            get = request.POST.get('idprog')
            form = ZadathaFullForm( request.POST, instance=CRM_Zadatha.objects.get(id= get) )
            if form.is_valid():
                c = form.save(commit=False)
                c.zakaz = lid
                c.save()
        # Новая задача
        elif tip == "form3":
            form = ZadathaFullForm(request.POST)
            if form.is_valid():
                c = form.save(commit=False)
                c.zakaz = lid
                c.created_by = request.user.first_name
                c.save()

        # Стаарый продукт 
        elif tip == "form6_old":
            get = CRM_Positions.objects.get(id=request.POST.get('ind')) 
            form = Positio_Form(request.POST , instance=get)
            if form.is_valid():
                c = form.save(commit=False)
                c.proz_nadb = round(sum([int(i)/100 for i in request.POST.getlist('nadb')] ),2)
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

        # Удалить 
        elif tip == 'form6_del_prod':
            get = request.POST.get('ind')
            f = CRM_Positions.objects.get(id=get)
            f.delete()

        return redirect(f'/zac/k/{pk}/')       
    else:
        form1 = Form_CRM_Zakaz(instance=lid)
        form3 = ZadathaFullForm()

        from4 = Docs_Form()
        from5 = Histori_Form()
        from6 = Positio_Form()
    return render(request, 'CRMzakaz/prodject-box.html',{'lid':lid ,'zad':zad, 'prod':prod, 'cont':cont , 'form4':from4 , 'form5':from5 , 'form6':from6 , 'form1':form1 , 'form3':form3})


