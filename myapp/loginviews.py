from django.contrib import messages
from django.shortcuts import redirect, render
from django.db import connection
from mysite.models import loginmodel
from rest_framework.response import Response
from django.contrib import messages
from rest_framework import status

def login(request):
    context={}
    if request.method=="POST":
            if request.POST.get('txt_loginName')and request.POST.get('txt_loginpwd'):
               checklogin=loginmodel
               checklogin.user=request.POST.get('txt_loginName')
               checklogin.password=request.POST.get('txt_loginpwd')
               cursor=connection.cursor()
               cursor.execute("select * from loginuser where user='"+ checklogin.user+"'and password='"+checklogin.password+"'")
               # cursor.execute("call checkuser('"+checklogin.user+"','"+checklogin.password+"')")
               # args = [checklogin.user, checklogin.password]
               # cursor.callproc('checkuser',args)
               result=cursor.fetchall()
               count=0
               for number in result:
                count=1
              
               if count>0: 
                  return redirect('dashboard')
               else:
                  messages.error(request,"invalid user name and password !")
                  return render(request, 'Admin/login.html',context)
                
    else: 
               return render(request,'Admin/login.html',context)

def dashboard(request):
    context={}
    return render(request,'Admin/dashboard.html',context)

