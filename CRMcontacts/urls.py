from django.urls import path
from .views import ( 
    contacts , contacts_all , contac_create,
    kompani , kompani_all , kompani_create
)

app_name='CRMcontacts'

urlpatterns = [
    path('all/', contacts_all, name='conall'),
    path('cd/<int:pk>/', contacts, name='contacts'),
    path('cd/', contac_create, name='contac_create'),
    
    path('kall/', kompani_all, name='kompani_all'),
    path('kd/<int:pk>/', kompani, name='kompani'),
    path('kd/', kompani_create, name='kompani_create'),

]

