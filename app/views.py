from django.shortcuts import render
from app.forms import *
# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponse




class Emp_Form(TemplateView):
    template_name='Emp_Form.html'
    def get_context_data(self,**kwargs):
        EDCO=super().get_context_data(**kwargs)
        EFO=EmployeeForm()
        EDCO['EFO']=EFO
        return EDCO

    def post(self,request):
        if request.method=='POST':
            EFD=EmployeeForm(request.POST)
            if EFD.is_valid():
                EFD.save()
                return HttpResponse('Data Insertted')