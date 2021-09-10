from decimal import Context
from django.db import connection
from mysite.models import usestoreprocesure
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from mysite.models import studentdetails
from mysite.serializers import studentserialize 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.core.files.storage import FileSystemStorage


from mysite.form import ImagefieldForm
from mysite.models import ImagefieldModel 

def home(request):
    context={}
    return render(request,'index.html',context)

def about(request):
    context={}
    return render(request,'aboutus.html',context)

def master(request):
    context={}
    return render(request,'index.html',context)

def is_admin(user):
    return user.groups.filter(name='ADMIN').exists()

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'Admin/dashboard.html')
    else:
        return render(request,'Student/studentafterlogin.html')

def storeprocedureuse(request):

    if request.method=="POST":
        if request.POST.get('fname')and request.POST.get('emailid')and request.POST.get('contactno') and request.POST.get('username'):
             enquiry=usestoreprocesure()
             enquiry.fullname=request.POST.get('fname')
             enquiry.email=request.POST.get('emailid')
             enquiry.contact=request.POST.get('contactno')
             enquiry.usernm=request.POST.get('username')
             enquiry.profilepic=request.POST.get('profilepic')
             cursor=connection.cursor()
             result=cursor.execute("call insertdata ('"+enquiry.fullname+"','"+enquiry.email+"','"+enquiry.contact+"','"+enquiry.usernm+"','"+enquiry.profilepic+"')")
             print(result)
             form = usestoreprocesure(request.POST, request.FILES)
            #  if form.is_valid():
             form.save()
             return render(request,'index.html')
        else:
            return render(request,'index.html')
    else:
        return render(request,'index.html')


@api_view(['POST'])
def saverecord(request):
    if request.method=="POST":
        form = studentserialize(request.POST, request.FILES)
        if form.is_valid():
           form.save()
    saveserialize=studentserialize(data=request.data)
    if saveserialize.is_valid():
          saveserialize.save()

        #   upload_file=request.POST.FILES['profilepic']
        #   fs=FileSystemStorage()
        #   fs.save(upload_file.name,upload_file)
         
    return Response(saveserialize.data,status=status.HTTP_201_CREATED)
    return Response(saveserialize.data,status=status.HTTP_400_BAD_REQUEST)

def home_view(request): 
    context = {}
    if request.method == "POST": 
        form = ImagefieldForm(request.POST, request.FILES) 
        if form.is_valid(): 
            title = form.cleaned_data.get("name") 
            img = form.cleaned_data.get("image_field") 
            obj = ImagefieldModel.objects.create( 
                                 title = title,  
                                 pic = img 
                                 ) 
            obj.save() 
            print(obj)
            return redirect('success') 
    else: 
        form = ImagefieldForm()
        context['form'] = form
        return render( request, "fileupload.html", context) 

def success(request): 
    return HttpResponse('successfully uploaded') 
    #return render(request, 'index.html')




        

     


