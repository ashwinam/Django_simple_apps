from typing import ContextManager
from django.shortcuts import render
from django.http import HttpResponse
from .models import MasterData, Student, Mark_Attendence
from .forms import StudentForm, StudentModelForm, MasterDataForm, MarkAttendenceForm, oneForm
from django.contrib import messages
import time

from Attendence import forms

# Create your views here.
def home(request):
    context = {'title':'Home Page'}
    return render(request, 'Attendence/base_page.html', context)

def atten(request):
    posts = Student.objects.all()
    return render(request, 'Attendence/test.html',{'title':'Student Data','data1':posts})

def name(request):
    return HttpResponse("<h1>Hello folkses</h1>")

posts = [{
    'Name':'Ashwin',
    'Addr':'Chanda',
    'phone_nm': 123456
},
{
   'Name':'Mohan',
    'Addr':'Vijaywada',
    'phone_nm': 123456 
}]

def Display_Tab(request):
    context = {
        'title':"Person's Data",
        'data':posts
        }
    return render(request,'Attendence/test.html',context)


def student_form(request):
    form = StudentForm()
    context = {'form':form}
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            ID = form.cleaned_data.get('ID')
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            Class = form.cleaned_data.get('Class')
            Student.objects.create(st_id=ID,st_name=name,st_mail=email,st_class=Class)
            # return render(request, 'Attendence/success.html', {'name':name})
            messages.success(request, "Record Added !")
        else:
            messages.warning(request,"Error! Error! Error!")
    return render(request,'Attendence/student_form.html', context)

def studentModelForm(request):
    form = StudentModelForm()
    context = {'form':form}
    if request.method == 'POST':
        form = StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Record Added !")
        else:
            messages.warning(request,"Error! Error! Error!")
    return render (request, 'Attendence/student_form.html',context)

def masterDataForm(request):
    form = MasterDataForm()
    context = {'form':form, 'Heading': 'Enter Student Details'}
    if request.method == 'POST':
        form = MasterDataForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data.get('st_name')
            messages.success(request,f"Record Added {name}")
        else:
            messages.warning(request, form.errors)

    return render(request, 'Attendence/student_form.html', context)

def epochToHuman(tm):
    currTime = time.localtime(tm)
    return time.strftime("%d-%m-%Y-%H", currTime)

def markAttendenceForm(request):
    form = MarkAttendenceForm()
    context = {'form': form, 'Heading': 'Mark Your Attendence'}
    if request.method == 'POST':
        form = MarkAttendenceForm(request.POST)
        if form.is_valid():
            dataObj = form.save(commit=False)
            dataObj.time1 = int(time.time())
            dataObj.ip_address = request.META.get('REMOTE_ADDR')
            dataObj.platform = request.META.get('HTTP_USER_AGENT')
            dataObj.date1 = epochToHuman(dataObj.time1)
            form.save()
            messages.success(request,'Attendence Marked!')
            print(dataObj.platform)
        else:
            messages.warning(request, form.errors)

    return render(request, 'Attendence/student_form.html',context)

def markAttendence(request):
    posts = Mark_Attendence.objects.all()
    context = {'title':'Attendence Sheet', 'data':posts}
    return render(request, 'Attendence/Attendence.html', context)


# Single page Display Form & Data
def filterAttendenceData(request):
    form = oneForm()
    context = {'form' : form, 'Heading': 'Filter'}
    if request.method == 'POST':
        form = oneForm(request.POST)
        if form.is_valid():
            ID = form.cleaned_data.get('ID')
            masterD = MasterData.objects.filter(st_id = ID)[0]
            posts = Mark_Attendence.objects.filter(ID=masterD)
            context = {'form' : form, 'Heading': 'Filter','data':posts, 'title': 'Attendence'}
            return render(request, 'Attendence/Attendence.html', context)


    return render(request, 'Attendence/Attendence.html', context)
    


    # return render(request, 'Attendence/student_form.html',context)


