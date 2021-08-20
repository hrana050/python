
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views
from . import loginviews, student, courseview
from . import excelimportviews



urlpatterns=[

  # path('',views.master),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('adminlogin',loginviews.login,name='adminlogin'),
    #path('afterlogin', views.afterlogin_view),
    path('dashboard', loginviews.dashboard, name='dashboard'),
    path('studentlist', student.studentlist, name='studentlist'),
    path('addstudent', student.addstudent, name='addstudent'),
    path('addcourse', courseview.addcourse, name='addcourse'),
    url(r'^deletecourse/(?P<sno>\d+)/$', courseview.deletecourse, name='deletecourse'),
    url(r'^editcourse/(?P<sno>\d+)/$', courseview.editcourse, name='editcourse'),
    url('saverecord',views.saverecord,name='saverecord'),
    url('storeprocedureuse',views.storeprocedureuse,name='storeprocedureuse'),
    url('upload_excel',excelimportviews.upload_excel,name='upload_excel'),
    path('',views.master,name='master'),
  
]