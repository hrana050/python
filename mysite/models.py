from django.db import models

class studentdetails(models.Model):
    fname=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    emailid=models.CharField(max_length=500)
    contactno=models.CharField(max_length=200)
    profilepic=models.CharField(max_length=200)
   # profilepic=models.ImageField(upload_to='')

    class Meta:
        db_table="signup"

class loginmodel(models.Model):
    user=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    class Meta:
        db_table="loginuser"

class usestoreprocesure(models.Model):
    fullname=models.CharField(max_length=200)
    usernm=models.CharField(max_length=200)
    email=models.CharField(max_length=500)
    contact=models.CharField(max_length=200)
    #profilepic=models.CharField(max_length=200)
    img=models.ImageField(upload_to='')

class importexceltodb(models.Model):
      name=models.CharField(max_length=200)
      Emp_code=models.CharField(max_length=200)
      Education=models.CharField(max_length=200)
      contactno=models.CharField(max_length=200)
      class Meta:
          db_table="upload_Excel"


    