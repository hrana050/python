
from rest_framework import serializers
from mysite.models import studentdetails

class studentserialize(serializers.ModelSerializer):
    class Meta:
        model=studentdetails
        fields=  ('fname','username','emailid','contactno','profilepic')