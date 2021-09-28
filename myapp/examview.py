import json
from django.contrib import messages
from django.db.models.fields import NullBooleanField
from django.shortcuts import render,redirect
from mysite.models import Examsetup
import datetime
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def addexamset(request):
    context={}
    if request.method=="POST":
        if request.POST.get('txt_question')and request.POST.get('course'):
            exam=Examsetup()
            exam.Courseid=request.POST.get('course')
            exam.Questionno=1
            exam.Question=request.POST.get('txt_question')
            exam.op_1=request.POST.get('txt_opt_1')
            exam.op_2=request.POST.get('txt_opt_2')
            exam.op_3=request.POST.get('txt_opt_3')
            exam.op_4=request.POST.get('txt_opt_4')
            exam.op_Ans=request.POST.get('txt_opt_ans')
            exam.E_time=request.POST.get('txt_time')
            exam.action='insert'
            cursor=connection.cursor()
            cursor.callproc('crudexamset',[0,exam.Courseid,exam.Questionno,exam.Question,exam.op_1,exam.op_2,exam.op_3,exam.op_4,exam.op_Ans,exam.E_time,exam.action])
            result = cursor.fetchall()
        for result_1 in result: 
            count=1
            messages.success(request, "Exam")
            return render(request,'Admin/SetExam.html',{'result':result})
        else:
             messages.error(request,'')
             return render(request,'Admin/SetExam.html',context)
    else:
        cursor=connection.cursor()
        sno=0
        status=0
        cursor.callproc('CUSD_course',[sno,"",status,"list"])
        result=cursor.fetchall()
        for result_1 in result: 
            count=1
        return render(request,'Admin/SetExam.html',{'result':result})

def deleteexam(request,sno):
    cursor=connection.cursor()
    status=0
    cursor.callproc('crudexamset',[sno,'""',status,'delete'])
    connection.close()
    return redirect('addcourse')

def editcourse(request,sno):
    cursor=connection.cursor()
    status=0
    cursor.callproc('CUSD_course',[sno,'""',status,'edit'])
    for result in cursor.fetchall(): 
        for values in result:
           data = {
            'my_data':result
         }
    return JsonResponse(data)

@csrf_exempt
def updatecourse(request): 
    if request.method=="POST":
        if request.POST.get('coursevalue')and request.POST.get('status'):
           stu_coursename=request.POST.get('coursevalue')
           stu_status=request.POST.get('status')
           stu_sno=request.POST.get('sno')
           cursor=connection.cursor()
           cursor.execute("call CUSD_course ('"+stu_sno+"','"+stu_coursename+"','"+stu_status+"','update')")
           connection.close()
           data = {
            'my_data':1
           }
           return JsonResponse(data)
        else:
           data = {
            'my_data':"error"
           }
        return JsonResponse(data)
    else:
         data = {
            'my_data':"fillfield"
           }
    return JsonResponse(data)

   
