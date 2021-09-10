import json
from django.contrib import messages
from django.db.models.fields import NullBooleanField
from django.shortcuts import render,redirect
from mysite.models import addcoursemodel
import datetime
from django.db import connection
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def addcourse(request):
    context={}
    if request.method=="POST":
        if request.POST.get('txt_course'):
            course=addcoursemodel()
            course.cousename=request.POST.get('txt_course')
            course.status=request.POST.get('status')
            course.action='insert'
            cursor=connection.cursor()
            cursor.callproc('CUSD_course',[0,course.cousename,course.status,course.action])
            result = cursor.fetchall()
        for result_1 in result: 
            count=1
            messages.success(request, course.cousename)
            return render(request,'Admin/course.html',{'result':result})
        else:
             messages.error(request,'')
             return render(request,'Admin/course.html',context)
    else:
        cursor=connection.cursor()
        sno=0
        status=0
        cursor.callproc('CUSD_course',[sno,"",status,"list"])
        result=cursor.fetchall()
        for result_1 in result: 
            count=1
        return render(request,'Admin/course.html',{'result':result})
def deletecourse(request,sno):
    cursor=connection.cursor()
    status=0
    cursor.callproc('CUSD_course',[sno,'""',status,'delete'])
    connection.close()
    return redirect('addcourse')

def editcourse(request,sno):
    print(sno)
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

   
