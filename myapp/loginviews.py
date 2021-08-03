from django.shortcuts import render
from django.db import connection
from mysite.models import loginmodel




def login(request):
    context={}
    return render(request,'Admin/login.html',context)


def dashboard(request):
    context={}
    if request.method=="POST":
        if request.POST.get('txt_loginName')and request.POST.get('txt_loginpwd'):
            checklogin=loginmodel
            checklogin.user=request.POST.get('txt_loginName')
            checklogin.password=request.POST.get('txt_loginpwd')
            cursor=connection.cursor()
            #valid=loginmodel(checklogin.user,checklogin.password)
            valid=cursor.callproc('checkuser',(checklogin.user,checklogin.password))
            cursor.close()
            if valid is not None:
             return render(request, 'Admin/dashboard.html',context)
            else:
                return render(request, 'Admin/dashboard.html',context) 
        else:
             return render(request, 'Admin/login.html',context)
    else:
        return render(request, 'Admin/login.html',context)
        #  cursor.close()
        
