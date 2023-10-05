"""
URL configuration for project35 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('fbv_string/',fbv_string,name='fbv_string'),
    path('Cbv_string/',Cbv_string.as_view(),name='Cbv_string'),


    path('fbv_page/',fbv_page,name='fbv_page'),
    path('Cbv_page/',Cbv_page.as_view(),name='Cbv_page'),


    path('insert_by_fbv/',insert_by_fbv,name='insert_by_fbv'),
    path('Insert_by_cbv/',Insert_by_cbv.as_view(),name='Insert_by_cbv'),

    path('CBV_Temp/',CBV_Temp.as_view(),name='CBV_Temp'),















]

