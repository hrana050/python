import io
from django import forms
from django.contrib import messages
from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.db import connection
from mysite.models import loginmodel, studentmodel
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
from mysite.serializers import updatestudent 
import datetime 
import os
from django.db import models

def addstudent(request):   
    context={}
    if request.method == "POST" and 'profile' in request.FILES:
       file, fileExtension = os.path.splitext(request.FILES['profile'].name)
       get_file_path(request.FILES['profile'].name)
       #print(file)
       #print(fileExtension)
    if request.method=="POST":
        if request.POST.get('txt_f_name')and request.POST.get('txt_l_name'):
             enquiry=studentmodel()
             enquiry.firstname=request.POST.get('txt_f_name')
             enquiry.lastname=request.POST.get('txt_l_name')
             enquiry.idno=request.POST.get('txt_id')
             enquiry.userid=request.POST.get('txt_userid')
             enquiry.password=request.POST.get('txt_pwd')
             enquiry.emailid=request.POST.get('txt_email')
             enquiry.contactno=request.POST.get('txt_contact')
             enquiry.year=request.POST.get('stu_year')
             enquiry.dob=request.POST.get('txt_dob')
             enquiry.course=int(request.POST.get('stu_course'))
             enquiry.address=request.POST.get('address')
             enquiry.profilepic=request.FILES['profile']
             enquiry.status=int(request.POST.get('stu_status'))
             enquiry.createdon=datetime.date.today()
             if len(request.FILES) !=0:
                 enquiry.profilepic=request.FILES['profile']
             enquiry.save()
             messages.success(request,enquiry.firstname)
             return render(request, 'Admin/Addstudent.html',context)
        else:
             messages.error(request, "Please fill the field...!")
             return render(request, 'Admin/Addstudent.html',context)          
    else: 
            cursor = connection.cursor()
            cursor.callproc('CUSD_course',[0,"",0,"list"])
            result = cursor.fetchall()
            for result_1 in result: 
                count=1
                connection.close()
            return render(request,'Admin/Addstudent.html',{'records':result})

def studentlist(request):
     context={} 
     cursor=connection.cursor()
     cursor.callproc('insertstudent',[0,'','','','','','','','','',0,'','',0,'list'])
     results_1 = cursor.fetchall()
     print(results_1)
     for result in results_1:
        connection.close()
        return render(request, 'Admin/studentlist.html',{'result':results_1})

def editstudent(request,sno):
    cursor=connection.cursor()
    cursor.callproc('insertstudent',[sno,'','','','','','','','','',0,'','',0,'edit'])

    for result in cursor.fetchall():
        data = {
            'my_data':result
    }
    return JsonResponse(data)

def edit(request,sno):
    cursor=connection.cursor()
    sno=0
    status=0
    cursor.callproc('CUSD_course',[sno,"",status,"list"])
    results_1 = cursor.fetchall()
    for result in results_1: 
        connection.close()
    return render(request, 'Admin/Addstudent.html',{'records':results_1})

def cancel(request):
    return redirect('studentlist')

def deletestudent(request,sno):
    cursor=connection.cursor()
    status=0
    cursor.callproc('insertstudent',[sno,'','','','','','','','','',0,'','',0,'delete'])
    connection.close()
    return redirect('studentlist')

def get_file_path(filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (3, ext)
    return os.path.join('profile/', filename)

