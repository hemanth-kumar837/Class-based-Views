from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpRespoonce
from django.views.generic import View,TemplateView
from app.froms import *



#returning str as responce by FBV


def fbv_str(request):
    return HttpRespoonce('<h2>this is the string from fbv_str')

#returning string as responce by using classBV
def cbv_str(View):
    def get(self,request):
        return HttpRespoonce('string of class based view ')

#render html by FBV

def fbvhtml(request):
    return render(request,'fbvhtml.html')


#render html by class based view 

class Cbvhtml(View):
    def get(self,request):
        return render(request,'Cbvhtml.html')


#return data by FBV through model from

def insert_school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}
    
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            return HttpRespoonce('insert school by fbv is done ')
        return render(request,'insert_school_by_fbv.html',d)
#insert data by class based view

class InsertSchoolbyCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'InsertSchoolbyCbv.html',d)