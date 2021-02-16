from django.urls import path
from .views import main , logins , logout_view , prodaja , create , my_prod

app_name='CRMmain'

urlpatterns = [
    path('', main, name='main'),
    path('lg/', logins, name='logins'),
    path("lo/", logout_view , name='logouto' ),
    path('kk/<int:pk>/', prodaja, name = 'prod'),
    path('my/', my_prod, name = 'my_prod'),
    path('cr/', create, name='create'),
]








