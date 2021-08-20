from django.contrib import messages
from django.shortcuts import render,redirect
from mysite.models import addcoursemodel
import datetime
from django.db import connection

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

def editcourse(request,sno):
    cursor=connection.cursor()
    cursor.execute("select * from addcourse where sno='"+sno+"'")
    result=cursor.fetchall()
    connection.close()
    return render(request,'Admin/course.html',{'editdata':result})
    # return redirect('addcourse',{'result':result})
