

from django.urls import path
from .views import mytask , email , ccalendar

app_name='CRMdashbord'

urlpatterns = [
    path('', mytask, name='mytask'),
    path('em/', email , name='email'),
    path('cal/' , ccalendar , name = 'cal')
    
]
