from decimal import Context
from django.db import connection
from mysite.models import usestoreprocesure
from django.http import response
from django.shortcuts import render
from django.contrib import messages
from mysite.models import studentdetails
from mysite.serializers import studentserialize 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage



def home(request):
    context={}
    return render(request,'index.html',context)


def about(request):
    context={}
    return render(request,'aboutus.html',context)

def master(request):
    context={}
    return render(request,'index.html',context)

def storeprocedureuse(request):
    context={}
    if request.method=="POST":
           if request.POST.get('fname')and request.POST.get('emailid')and request.POST.get('contactno') and request.POST.get('username'):
             enquiry=usestoreprocesure()
             enquiry.fullname=request.POST.get('fname')
             enquiry.email=request.POST.get('emailid')
             enquiry.contact=request.POST.get('contactno')
             enquiry.usernm=request.POST.get('username')
             enquiry.img=request.POST.get('profilepic')
             cursor=connection.cursor()
             cursor.execute("call insertdata ('"+enquiry.fullname+"','"+enquiry.email+"','"+enquiry.contact+"','"+enquiry.usernm+"','"+enquiry.img+"')")
             form = usestoreprocesure(request.POST, request.FILES)
             if form.is_valid():
                form.save()
                messages.success(request,"Student Enquiry submitted ")
                return render(request,'index.html')


@api_view(['POST'])
def saverecord(request):
    if request.method=="POST":
    #      form = studentserialize(request.POST, request.FILES)
    # if form.is_valid():
    #    form.save()
     saveserialize=studentserialize(data=request.data)
    if saveserialize.is_valid():
          saveserialize.save()

        #   upload_file=request.POST.FILES['profilepic']
        #   fs=FileSystemStorage()
        #   fs.save(upload_file.name,upload_file)
         
    return Response(saveserialize.data,status=status.HTTP_201_CREATED)
    return Response(saveserialize.data,status=status.HTTP_400_BAD_REQUEST)
  #  return render(request, 'index.html')




        

     


