from django.contrib import messages
from django.shortcuts import render,redirect
from mysite.models import addcoursemodel
import datetime
from django.db import connection
from django.http import JsonResponse

def addcourse(request):
    context={}
    if request.method=="POST":
        if request.POST.get('txt_course'):
            course=addcoursemodel()
            course.cousename=request.POST.get('txt_course')
            course.status=int(request.POST.get('status'))
            course.createdon=datetime.date.today()
            course.save()
            cursor=connection.cursor()
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
        cursor.execute('select * from addcourse')
        result=cursor.fetchall()
        connection.close()
        return render(request,'Admin/course.html',{'result':result})
def deletecourse(request,sno):
    cursor=connection.cursor()
    cursor.execute("delete from addcourse where sno='"+sno+"'")
    result=cursor.fetchall()
    connection.close()
    return redirect('addcourse')

# def editcourse(request,sno):
#     cursor=connection.cursor()
#     cursor.execute("select * from addcourse where sno='"+sno+"'")
#     result=cursor.fetchall()
#     connection.close()
#     cursor = connection.cursor()
#     cursor.execute("select * from addcourse")
#     records1 = cursor.fetchall()
#     context={'editdata':result, 'result':records1}
#     return render(request,'Admin/course.html',context)
def editcourse(request,sno):
    cursor=connection.cursor()
    cursor.execute("select * from addcourse where sno='"+sno+"'")
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

def updatecourse(request,coursedata):
    print(coursedata)
    if request.method=="POST":
        if request.POST.get('txt_course')and request.POST.get('status'):
           course=addcoursemodel()
           course.cousename=request.POST.get('txt_course')
           print(course.cousename)
           course.status=int(request.POST.get('status'))
           cursor=connection.cursor()
           cursor.execute("update addcourse set cousename='"+course.cousename+"',status='"+course.status+"'where sno='"+1+"'")
           result=cursor.fetchall()
           connection.close()
           data = {
            'my_data':result
           }
           return JsonResponse(data)
        else:
           data = {
            'my_data':"error"
           }
    else:
         data = {
            'my_data':"fillfield"
           }

   
