from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.core.mail import send_mail , send_mass_mail
from django.db.models import Q
#from datetime import datetime , timedelta 
#import openpyxl
#import pytz
#import calendar

from .models import CRM_Contacts, CRM_Kompani
from .forms import ContactsForm , KompaniForm , ContactsFulForm , KompaniFullForm

from CRMzadacha.forms import ZadathaForm , ZadathaFullForm
from CRMzadacha.models import CRM_Zadatha

from CRMmain.models import CRM_Lid_Zapros , CRM_Docs

from CRMzakaz.models import CRM_Zakaz



#  Все контакты 
@login_required(login_url='/lg/')
def contacts_all(request):
    cont = CRM_Contacts.objects.all()
    if request.method == 'POST':
        form = ContactsForm( request.POST )
        if form.is_valid():
            form.save()
        return redirect('CRMcontacts:conall')
    else:
        form = ContactsForm()
    return render(request, 'CRMcontacts/contacts_all.html',{'cont': cont  , 'form': form})

#  Контакт 
@login_required(login_url='/lg/')
def contacts(request, pk):
    cont = CRM_Contacts.objects.get(id = pk)
    conact = CRM_Zadatha.objects.filter(conact=cont)
    if request.method == 'POST':
        tip = request.POST.get('form')
        if tip == "form1":
            form = ContactsForm( request.POST, instance=cont )
            if form.is_valid():
                form.save()
        #  Старые задачи
        elif tip == "form2":
            get = request.POST.get('idprog')
            form = ZadathaFullForm( request.POST, instance=CRM_Zadatha.objects.get(id= get) )
            if form.is_valid():
                c = form.save(commit=False)
                c.conact = cont
                c.save()
        # Новая задача
        elif tip == "form3":
            form = ZadathaFullForm(request.POST)
            if form.is_valid():
                c = form.save(commit=False)
                c.conact = cont
                c.created_by = request.user.first_name
                c.save()
        elif tip == "form4":
            form = ContactsFulForm( request.POST, instance=cont )
            if form.is_valid():
                form.save()
           

        return  redirect(f'/c/cd/{pk}/')
    else:
        form = ContactsForm(instance=cont)
        from3 = ZadathaFullForm()
        form4 = ContactsFulForm(instance=cont)

    return render(request, 'CRMcontacts/contacts.html', {'form4':form4, 'form': form ,'form3': from3 ,  "conta":cont , 'conact':conact})

#  Контакт  создать 
@login_required(login_url='/lg/')
def contac_create(request):
    if request.method == 'POST':
        form = ContactsForm( request.POST )
        if form.is_valid():
            form.save()
        return redirect('CRMcontacts:conall')
    else:
        form = ContactsForm()
    return render(request, 'CRMcontacts/contacts.html', {'form': form})

#  Все компании  
@login_required(login_url='/lg/')
def kompani_all(request):
    comp = CRM_Kompani.objects.all()
    if request.method == 'POST':
        form = KompaniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('CRMcontacts:kompani_all')
    else:
        form = KompaniForm()
    return render(request, 'CRMcontacts/kompanis_all.html',{'cont': comp , 'form':form})

#  Компания 
@login_required(login_url='/lg/')
def kompani(request, pk):
    conta = CRM_Kompani.objects.get(id = pk)
    cont = CRM_Contacts.objects.filter(compani__id=pk)
    
    if request.method == 'POST':
        get = request.POST.get('form')
        if get == 'form1':
            form = KompaniFullForm( request.POST, instance=conta )
            if form.is_valid():
                form.save()
        elif get == 'form2':
            get = request.POST.get('idprog')
            form = ZadathaForm( request.POST, instance=CRM_Zadatha.objects.get(id= get) )
            if form.is_valid():
                form.save()
        return redirect(f'/c/kd/{pk}/')
    else:
        form = KompaniFullForm(instance=conta)
    return render(request, 'CRMcontacts/kompanis.html', {'form': form ,'cont':cont , 'conta':conta})

#  Компания  создать 
@login_required(login_url='/lg/')
def kompani_create(request):
    if request.method == 'POST':
        form = KompaniForm( request.POST )
        if form.is_valid():
            form.save()
        return redirect('CRMcontacts:kompani_all')
    else:
        form = KompaniForm()
    return render(request, 'CRMcontacts/kompanis.html', {'form': form})





