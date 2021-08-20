from django.contrib import messages
from django.shortcuts import redirect, render
from django.db import connection
from mysite.models import loginmodel, studentmodel
from rest_framework.response import Response
from rest_framework import status
from django.core.files.storage import FileSystemStorage
import os
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
             enquiry.password=request.POST.get('txt_email')
             enquiry.emailid=request.POST.get('txt_pwd')
             enquiry.contactno=request.POST.get('txt_contact')
             enquiry.year=request.POST.get('stu_year')
             enquiry.dob=request.POST.get('txt_dob')
             enquiry.course=int(request.POST.get('stu_course'))
             enquiry.address=request.POST.get('address')
             enquiry.profilepic=request.FILES['profile']
             fs=FileSystemStorage()
             fs.save(enquiry.profilepic.name,enquiry.profilepic)
             enquiry.status=int(request.POST.get('stu_status'))
             enquiry.createdon=datetime.date.today()
             enquiry.save()
             cursor=connection.cursor()
             cursor.execute("select sno  from addstudent order by sno desc  LIMIT 1")
             result=cursor.fetchall()
             connection.close()
             count=0
             for number in result:
                 print(number[0])
                 count=1
             if count==1:
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
