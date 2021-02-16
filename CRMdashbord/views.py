from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from CRMzadacha.forms import ZadathaForm , ZadathaFullForm
from CRMzadacha.models import CRM_Zadatha
from CRMmain.models import CRM_Lid_Zapros , CRM_Docs


@login_required(login_url='/lg/')
def mytask(request):
    


    return render(request, 'CRMdashbord/main.html',{'zada': 'zad' , "form1":'form1'})


@login_required(login_url='/lg/')
def email(request):
    
    return render(request, 'CRMdashbord/email.html',{'zada': 'zad' , "form1":'form1'})



@login_required(login_url='/lg/')
def  ccalendar(request):
    
    return render(request, 'CRMdashbord/calendar.html',{'zada': 'zad' , "form1":'form1'})



