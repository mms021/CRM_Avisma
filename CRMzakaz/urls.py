
from django.urls import path
from .views import main  , zakaz

app_name='CRMzakaz'

urlpatterns = [
    path('', main, name='main'),
    path('k/<int:pk>/', zakaz, name = 'zak'),
]


















