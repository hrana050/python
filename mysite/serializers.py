
from rest_framework import serializers
from django.forms import ModelForm
from mysite.models import studentdetails,studentmodel

class studentserialize(serializers.ModelSerializer):
    class Meta:
        model=studentdetails
        fields=  ('fname','username','emailid','contactno','profilepic')

class updatestudent(ModelForm):
    class Meta:
        model=studentmodel
        fields= '__all__'