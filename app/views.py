from django.shortcuts import render
from app.views import *
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def application_forms(request):
    ATFO= departmentForms()
    d={'ATFO':ATFO}
    if request.method=='POST':
        AEDO = departmentForms(request.POST)
        if AEDO.is_valid():
            AEDO.save()
            return HttpResponse('application done.......')
    return render (request,'application_forms.html',d)

def Docotor_file(request):
    EMTO= DoctorForms()
    d={'EMTO':EMTO}
    if request.method== 'POST':
        DOCT=DoctorForms(request.POST)
        if DOCT.is_valid():
            DOCT.save()
            return HttpResponse('DOCTOR application Done...')
    return render(request,'Docotor_file.html',d)


def patient_forms(request):
    APCO=patientforms()
    d={'APCO':APCO}
    if request.method =='POST':
        APFC=patientforms(request.POST)
        if APFC.is_valid():
            APFC.save()
            return HttpResponse('Appication succcessfully.....')
    return render (request,'patient_forms.html',d)

def appoint_ment(request):
    AMFO=AM_forms()
    d={'AMFO':AMFO}
    if request.method == 'POST':
        AFCD=AM_forms(request.POST)
        if AFCD.is_valid():
            AFCD.save()
            return HttpResponse('appointment form complted.......')
    return render(request,'appoint_ment.html',d)

