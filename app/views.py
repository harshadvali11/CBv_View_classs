from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# FBV for returing String

def fbv_string(request):
    return HttpResponse('This is FBV String')

# CBV for returing String

class Cbv_string(View):
    def get(self,request):
        return HttpResponse('Cbv_string')


# rendering html page by using FBV

def fbv_page(request):
    return render(request,'fbv_page.html')


# rendering html by CBV
class Cbv_page(View):
    def get(self,request):
        return render(request,'Cbv_page.html')


# insert data by using FBV


def insert_by_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Is Inserted')
    return render(request,'insert_by_fbv.html',d)

#Insert_by_cbv

class Insert_by_cbv(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'Insert_by_cbv.html',d)
    
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data Is Inserted')
        


# Render Html page by using TemplateView

class CBV_Temp(TemplateView):
    template_name='CBV_Temp.html'











































