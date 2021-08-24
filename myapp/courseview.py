import json
from django.contrib import messages
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
            cursor=connection.cursor()
            cursor.execute("call insertcourse ('"+course.cousename+"','"+course.status+"')")
            connection.close()
            cursor=connection.cursor()
            #cursor.execute("call getcourselist")
            cursor.execute('select * from addcourse')
            result=cursor.fetchall()
            connection.close()
            messages.success(request, course.cousename)
            return render(request,'Admin/course.html',{'result':result})
        else:
             messages.error(request,'')
             return render(request,'Admin/course.html',context)
    else:
        cursor=connection.cursor()
        #cursor.execute("call getcourselist()")
        cursor.execute('select * from addcourse')
        result=cursor.fetchall()
        connection.close()
        return render(request,'Admin/course.html',{'result':result})
def deletecourse(request,sno):
    cursor=connection.cursor()
    cursor.execute("call deletecourse ('"+ sno +"')")
    connection.close()
    return redirect('addcourse')

def editcourse(request,sno):
    cursor=connection.cursor()
    cursor.execute("select * from addcourse where sno='"+ sno +"'")
    result=cursor.fetchall()
    connection.close()
    for values in result:
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
           cursor.execute("call updatecourse ('"+stu_sno+"','"+stu_coursename+"','"+stu_status+"')")
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

   
