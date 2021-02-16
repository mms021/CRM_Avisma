from django.shortcuts import render ,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from CRMzadacha.forms import ZadathaForm , ZadathaFullForm
from CRMzadacha.models import CRM_Zadatha
from CRMmain.models import CRM_Lid_Zapros

@login_required(login_url='/lg/')
def mytask(request):
    zad = CRM_Zadatha.objects.exclude(chec='vi').filter(user=request.user)
    #zad = CRM_Zadatha.objects.exclude(chec='vi')
    if request.method == 'POST':
        
        get =CRM_Zadatha.objects.get(id= request.POST.get('idprog'))  
        form = ZadathaForm( request.POST, instance=get )
        if form.is_valid():
            form.save()

            lid = CRM_Lid_Zapros.objects.get(id = get.projects.id )
            if form.cleaned_data['chec'] =='vi' and form.cleaned_data['title'] == '3. Проверка технологических возможностей':
                    if lid.prov_na_nom < 9:
                        lid.prov_na_nom = lid.prov_na_nom + 1
                        lid.prov_na_sklade = None
                        lid.save()
        return redirect('CRMzadacha:mytask')
    else: 
        form1 = ZadathaFullForm()
    return render(request, 'CRMzadacha/my-tasks.html',{'zada': zad , "form1":form1})




