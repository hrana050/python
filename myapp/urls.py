
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views
from . import loginviews, student
from . import excelimportviews



urlpatterns=[

  # path('',views.master),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('adminlogin',loginviews.login,name='adminlogin'),
    #path('afterlogin', views.afterlogin_view),
    path('dashboard', loginviews.dashboard, name='dashboard'),
    path('addstudent', student.addstudent, name='addstudent'),
    url('saverecord',views.saverecord,name='saverecord'),
    url('storeprocedureuse',views.storeprocedureuse,name='storeprocedureuse'),
    url('upload_excel',excelimportviews.upload_excel,name='upload_excel'),
    path('',views.master,name='master'),
  
]