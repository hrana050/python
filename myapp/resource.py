from django.db import models
from import_export import resources
from mysite.models import importexceltodb

class excelupload(resources.ModelResource):
    class meta:
        models=importexceltodb