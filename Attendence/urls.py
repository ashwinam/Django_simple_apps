from django.urls.conf import path
from django.urls.resolvers import URLPattern
from . import views
from django.urls import path

urlpatterns = [
    path('', views.atten, name='atten'),
    path('name', views.name, name='name'),
    path('disp', views.Display_Tab, name='disp_tab'),
    path('studentForm', views.student_form, name='disp_form'),
    path('studentModelForm', views.studentModelForm, name='disp_student_form'),
    path('MasterForm', views.masterDataForm, name='masterForm'),
    path('AttendenceForm', views.markAttendenceForm, name='attendenceForm'),
    path('AttendenceSheet', views.markAttendence, name='attendencesheet'),
    path('filterAttendence', views.filterAttendenceData, name='filterData'),
]