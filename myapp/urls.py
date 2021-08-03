
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views
from . import loginviews
from . import excelimportviews


urlpatterns=[

  #  path('',views.master),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
   
    path('login/',loginviews.login,name='login'),
    path('dashboard',loginviews.dashboard,name='dashboard'),
    url('saverecord',views.saverecord,name='saverecord'),
    url('storeprocedureuse',views.storeprocedureuse,name='storeprocedureuse'),
    url('upload_excel',excelimportviews.upload_excel,name='upload_excel'),
     path('',views.master,name='master'),
   
]