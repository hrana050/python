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
            cursor.callproc('insertcoursedata',[0,course.cousename,course.status,course.action])
        for result in cursor.stored_results(): 
            results_1 = result.fetchall()
            connection.close()
            messages.success(request, course.cousename)
            return render(request,'Admin/course.html',{'result':results_1})
        else:
             messages.error(request,'')
             return render(request,'Admin/course.html',context)
    else:
        cursor=connection.cursor()
        sno=0
        status=0
        cursor.callproc('insertcoursedata',[sno,"",status,"list"])
        for result in cursor.stored_results(): 
            results_1 = result.fetchall()
        connection.close()
        return render(request,'Admin/course.html',{'result':results_1})
def deletecourse(request,sno):
    cursor=connection.cursor()
    status=0
    cursor.callproc('insertcoursedata',[sno,'""',status,'delete'])
    connection.close()
    return redirect('addcourse')

def editcourse(request,sno):
    cursor=connection.cursor()
    status=0
    cursor.callproc('insertcoursedata',[sno,'""',status,'select'])
    for result in cursor.stored_results(): 
        results_1 = result.fetchall()
    connection.close()
    for values in results_1:
        values[1]
        values[2]
        values[0]
    data = {
            'my_data':values
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
           cursor.execute("call insertcoursedata ('"+stu_sno+"','"+stu_coursename+"','"+stu_status+"','update')")
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

   
