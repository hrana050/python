from decimal import Context
from django.contrib import messages
from django.shortcuts import redirect, render
from django.db import connection
from mysite.models import loginmodel
from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status
import os
def login(request):
    context={}
    if request.method=="POST":
            if request.POST.get('txt_loginName')and request.POST.get('txt_loginpwd'):
               checklogin=loginmodel
               checklogin.user=request.POST.get('txt_loginName')
               checklogin.password=request.POST.get('txt_loginpwd')
               cursor=connection.cursor()
               args = (checklogin.user,checklogin.password)
               cursor.callproc('checkuser',args)
               count=0
               results_1 = cursor.fetchall()
               for number in results_1:
                   count=1
                   request.session['usersessionid']=number[0]
                   request.session['usersessionname']=number[6]
                   connection.close()
               if count>0: 
                  return redirect('dashboard')
               else:
                  messages.error(request,"invalid user name and password !")
                  return render(request, 'Admin/login.html',context)
            else:
                messages.error(request,"Enter the username and password !")
                return render(request,'Admin/login.html',context)
                
    else: 
               return render(request,'Admin/login.html',context)

def dashboard(request):
    context={}
    return render(request,'Admin/dashboard.html',context)
   
def logout(request):
   context={}
   del request.session['usersessionid']
   del request.session['usersessionname']
   return redirect('adminlogin')

def studentlogin(request):
    context={}
    if request.method=="POST":
            if request.POST.get('txt_loginName')and request.POST.get('txt_loginpwd'):
               checklogin=loginmodel
               checklogin.user=request.POST.get('txt_loginName')
               checklogin.password=request.POST.get('txt_loginpwd')
               cursor=connection.cursor()
               args = (checklogin.user,checklogin.password)
               cursor.callproc('checkstudentlogin',args)
               count=0
               results_1 = cursor.fetchall()
               for number in results_1:
                   count=1
                   request.session['usersessionid']=number[0]
                   request.session['usersessionname']=number[1]
                   connection.close()
               if count>0: 
                  return redirect('studentdashboard')
               else:
                  messages.error(request,"invalid user name and password !")
                  return render(request, 'student/login.html',context)
            else:
                messages.error(request,"Enter the username and password !")
                return render(request,'student/login.html',context)
                
    else: 
               return render(request,'student/login.html',context)


def studentdashboard(request):
    context={}
    return render(request,'student/dashboard.html',context)
   
def studentlogout(request):
   context={}
   del request.session['usersessionid']
   del request.session['usersessionname']
   return redirect('studentlogin')


