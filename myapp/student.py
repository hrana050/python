import io
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db import connection
from mysite.models import loginmodel, studentmodel,Person
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
import os
import datetime
import hashlib
from django.core.files.base import ContentFile
from django.core.exceptions import ValidationError

def addstudent(request):    
    context={} 
    if request.method=="POST":
        if request.POST.get('txt_f_name')and request.POST.get('txt_l_name'):
             enquiry=studentmodel()
             enquiry.firstname=request.POST.get('txt_f_name')
             enquiry.lastname=request.POST.get('txt_l_name')
             enquiry.idno=request.POST.get('txt_id')
             enquiry.userid=request.POST.get('txt_userid')
             enquiry.password=request.POST.get('txt_email')
             enquiry.emailid=request.POST.get('txt_pwd')
             enquiry.contactno=request.POST.get('txt_contact')
             enquiry.year=request.POST.get('stu_year')
             enquiry.dob=request.POST.get('txt_dob')
             enquiry.course=int(request.POST.get('stu_course'))
             enquiry.address=request.POST.get('address')
             enquiry.profilepic=request.FILES['profile']
             enquiry.filename=" "
             enquiry.status=int(request.POST.get('stu_status'))
             cursor=connection.cursor()
             cursor.callproc('insertstudent',[enquiry.firstname,enquiry.lastname,enquiry.idno, enquiry.userid,
             enquiry.emailid,enquiry.password,enquiry.contactno,enquiry.year,enquiry.dob,enquiry.course,enquiry.address,
             enquiry.filename,enquiry.status])
             count=0
             for result in cursor.stored_results(): 
                 results_1 = result.fetchall()
             for values in results_1:
                 values[0]
                 enquiry=Person()
                 enquiry.photo=request.FILES['profile']
                 enquiry.save()
                    
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
            cursor.execute('select * from addcourse')
            records = cursor.fetchall()
            return render(request,'Admin/Addstudent.html',{'records':records})

def studentlist(request):
     context={} 
     cursor=connection.cursor()
     cursor.execute("select *  from addstudent")
     result=cursor.fetchall()
     connection.close()
     count=0
     for number in result:
         print(number[0])
     return render(request, 'Admin/studentlist.html',{'result':result})

