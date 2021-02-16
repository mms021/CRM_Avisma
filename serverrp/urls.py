"""serverrp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('CRMmain.urls')),
    path('c/', include('CRMcontacts.urls')),
    path('z/', include('CRMzadacha.urls')),
    path('d/', include('CRMdashbord.urls')),
    path('zac/', include('CRMzakaz.urls'))
    # path('ad/',include('glavarp.urls')),
    # path('a/',include('resurses.urls')),
    # path('p/',include('post.urls')),
    # path('preseil/',include('preseil.urls')),
    # path('plan/',include('resorsplaning.urls')),
    # path('ut/',include('ushetvremeni.urls')),
    # path('b/',include('bazaznaniy.urls')),
    
    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
