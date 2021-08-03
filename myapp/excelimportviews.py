from mysite.models import importexceltodb
from .resource import excelupload
from tablib import Dataset
from django.shortcuts import render
from django.contrib import messages


def upload_excel(request):
    if request.method=="POST":
        excel_resouces=excelupload()
        dataset = Dataset()
        (new_person)=request.FILES['myfile']

        if not new_person.name.endswith('xlsx'):
          messages.info(request,'wrong format')
          return render(request,'uploadexcel.html')

        import_data=dataset.load(new_person.read(),format='xlsx')
        for data in import_data:
            value = importexceltodb(data[0],data[1],data[2],data[3],data[4])
            value.save()
    return render(request,'uploadexcel.html')