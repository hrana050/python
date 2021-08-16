from django.contrib import messages
from django.shortcuts import redirect, render
from django.db import connection
from mysite.models import loginmodel, studentmodel
from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status


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
             enquiry.course=request.POST.get('stu_course')
             enquiry.address=request.POST.get('address')
             enquiry.profilepic=request.POST.get('profilepic')
             enquiry.status=request.POST.get('stu_status')
             cursor=connection.cursor()
             cursor.execute("call insertdata ('"+enquiry.firstname+"','"+enquiry.lastname+"','"+enquiry.idno+
                                                     "','"+enquiry.userid+"','"+enquiry.emailid+"','"+enquiry.password+
                                                     "','"+ enquiry.contactno+"','"+ enquiry.year+"','"+ enquiry.dob+
                                                     "','"+ enquiry.course+"','"+ enquiry.address+"','"+ enquiry.profilepic+"','"+enquiry.status+"')")
             result=cursor.fetchall()
             count=0
             for number in result:
                cursor.execute("update  addstudent profilepic='"+number[0]+"' where sno='"+ number[0]+"'")
                count=1
                if count>0:
                           messages.success(request, "Student details submit successfully. !")
                           return render(request, 'Admin/Addstudent.html',context)
                else:
                           messages.error(request, "Please fill the correct information. !")
                           return render(request, 'Admin/Addstudent.html',context)
        else:
             return render(request, 'Admin/Addstudent.html',context)          
    else: 
             return render(request,'Admin/Addstudent.html',context)