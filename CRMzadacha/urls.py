from django.urls import path
from .views import mytask

app_name='CRMzadacha'

urlpatterns = [
    path('', mytask, name='mytask'),
    
]


