import os
from uuid import uuid4
from django.db import models
from django.db.models.fields import CharField, IntegerField
from django.db import connection

class studentdetails(models.Model):
    fname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    emailid=models.CharField(max_length=500)
    contactno=models.CharField(max_length=200)
    #profilepic=models.CharField(max_length=200)
    profilepic=models.ImageField(upload_to='')

    class Meta:
        db_table="signup"

class loginmodel(models.Model):
    name=models.CharField(max_length=200)
    user=models.CharField(max_length=200)
    emailid=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    status=models.IntegerField

class usestoreprocesure(models.Model):
    fullname=models.CharField(max_length=200)
    usernm=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    contact=models.CharField(max_length=200)
    profilepic=models.CharField(max_length=200)
    #img=models.ImageField(upload_to='')

class importexceltodb(models.Model):
      name=models.CharField(max_length=200)
      Emp_code=models.CharField(max_length=200)
      Education=models.CharField(max_length=200)
      contactno=models.CharField(max_length=200)
      class Meta:
          db_table="upload_Excel"
class studentmodel(models.Model):
   firstname =models.CharField(max_length=200)
   lastname =models.CharField(max_length=200)
   idno =models.CharField(max_length=200)
   userid =models.CharField(max_length=500)
   emailid =models.CharField(max_length=500)
   password=models.CharField(max_length=200)
   contactno =models.CharField(max_length=200)
   year =models.CharField(max_length=200)
   dob =models.CharField(max_length=200)
   course =models.IntegerField()
   address =models.CharField(max_length=6000)
   profilepic =models.ImageField(upload_to='')
   status=models.IntegerField()
   createdon=models.DateField()
   class Meta:
        db_table = "student"

class addcoursemodel(models.Model):
      sno=models.IntegerField()
      cousename=models.CharField(max_length=1000)
      status=models.IntegerField()
      createdon=models.DateField()
      action=models.CharField(max_length=200)

class ImagefieldModel(models.Model): 
    sno=IntegerField()
    title = models.CharField(max_length = 200) 
    pic = models.ImageField(upload_to = "profileimg/")

    class Meta:
        db_table = "insertimage"

class Examsetup(models.Model):
      Courseid=models.IntegerField()
      Questionno=models.IntegerField()
      Question=models.CharField(max_length=5000)
      op_1=models.CharField(max_length=2000)
      op_2=models.CharField(max_length=2000)
      op_3=models.CharField(max_length=2000)
      op_4=models.CharField(max_length=2000)
      op_Ans=models.CharField(max_length=2000)
      E_time=models.IntegerField()
      action=models.CharField(max_length=200)
      



    