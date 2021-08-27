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

def addstudent(request):   
    context={}
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
             enquiry.save()
             cursor=connection.cursor()
             cursor=connection.cursor()
             cursor.callproc('getstudentsno')
             count=0
             for result in cursor.stored_results(): 
                 results_1 = result.fetchall()
             for values in results_1:
                 count=1
             if count>0:
                           messages.success(request, enquiry.firstname)
                           return render(request, 'Admin/Addstudent.html',context)
             else:
                           messages.error(request, enquiry.firstname)
                           return render(request, 'Admin/Addstudent.html',context)
        else:
             messages.error(request, "Please fill the field...!")
             return render(request, 'Admin/Addstudent.html',context)          
    else: 
            cursor = connection.cursor()
            cursor.callproc('insertcoursedata',[0,"",0,"list"])
            for result in cursor.stored_results(): 
                results_1 = result.fetchall()
                connection.close()
            return render(request,'Admin/Addstudent.html',{'records':results_1})

def studentlist(request):
     context={} 
     cursor=connection.cursor()
     cursor.callproc('insertstudent',[0,'','','','','','','','','',0,'','',0,'list'])
     for result in cursor.stored_results(): 
        results_1 = result.fetchall()
        connection.close()
        for values in results_1:
         return render(request, 'Admin/studentlist.html',{'result':results_1})

def editstudent(request,sno):
    cursor=connection.cursor()
    cursor.callproc('insertstudent',[sno,'','','','','','','','','',0,'','',0,'getdetails'])
    for result in cursor.stored_results(): 
        results_1 = result.fetchall()
    connection.close()
    for values in results_1:
        values[0],values[1],values[2],values[3],
        values[4],values[5],values[6],values[7],
        values[8],values[9],values[10],values[11],
        values[15]

    data = {
            'my_data':values
    }
    return JsonResponse(data)

def edit(request,sno):
    cursor=connection.cursor()
    sno=0
    status=0
    cursor.callproc('insertcoursedata',[sno,"",status,"list"])
    for result in cursor.stored_results(): 
        results_1 = result.fetchall()
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

def update(request):  
    t = studentmodel.objects.get(sno=76)
    form=updatestudent(instance=t)
    if forms.is_valid():
        form.save()
    return redirect('studentlist') 

