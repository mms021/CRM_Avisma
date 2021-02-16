from django.contrib import admin

# Register your models here.


from .models import CRM_Docs , CRM_Lid_Zapros , CRM_P_Postavka

admin.site.register(CRM_Docs)
admin.site.register(CRM_Lid_Zapros)
admin.site.register(CRM_P_Postavka)

