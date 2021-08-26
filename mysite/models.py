import os
from uuid import uuid4
from django.db import models
from django.db.models.fields import CharField
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
def rename_image(instance, filename):
    return instance + '.jpg'
def wrapper(instance, filename):
        print(filename)
        ext = filename.split('.')[-1]
        print(ext)
        # get filename
        if instance:
            filename = '{}.{}'.format(instance, ext)
            print(filename)
        else:
            # set filename as random string
            filename = '{}.{}'.format(uuid4().hex, ext)
        # return the whole path to the file
        return wrapper
    
class studentmodel(models.Model):
   sno =models.IntegerField()
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
   profilepic =models.ImageField(upload_to=wrapper)
   filename=CharField(max_length=200)
   status=models.IntegerField()
   createdon=models.DateField()
   class Meta:
        db_table = "addstudent"

def generate_unique_name(path,format):
        filesize = format.file.size
        print(filesize)

        return os.path.join(path, format)

class MyModel(models.Model):
    upload = models.ImageField(upload_to=generate_unique_name)
        


class addcoursemodel(models.Model):
      sno=models.IntegerField()
      cousename=models.CharField(max_length=1000)
      status=models.IntegerField()
      createdon=models.DateField()
      action=models.CharField(max_length=200)
import time
def upload_to(instance, filename):
    cursor=connection.cursor()
    result=cursor.execute("select sno  from addstudent order by sno desc  LIMIT 1")
    result.fetchall()
    for values in result:
        filename = values[0]
    #filename = time.strftime('%Y%m%d%H%M%S')
    ym = time.strftime('%Y%m')
    return '%s/%s.jpg' % (ym,filename)

class Person(models.Model):
      photo = models.ImageField(upload_to=upload_to)




    