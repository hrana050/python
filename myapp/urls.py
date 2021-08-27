
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
    path('logout',loginviews.logout,name='logout'),
    path('dashboard', loginviews.dashboard, name='dashboard'),
    path('addcourse', courseview.addcourse, name='addcourse'),
    url(r'^deletecourse/(?P<sno>\d+)/$', courseview.deletecourse, name='deletecourse'),
    url(r'^editcourse/(?P<sno>\d+)/$', courseview.editcourse, name='editcourse'),
    url('updatecourse', courseview.updatecourse, name='updatecourse'),
    path('addstudent', student.addstudent, name='addstudent'),
    path('studentlist', student.studentlist, name='studentlist'),
    url(r'^editstudent/(?P<sno>\d+)/$', student.editstudent, name='editstudent'),
    path('edit/<sno>', student.edit, name='edit'),
    url('cancel', student.cancel, name='cancel'), 
    url(r'^deletestudent/(?P<sno>\d+)/$', student.deletestudent, name='deletestudent'), 
    path('update', student.update,name='update'),
    path('',views.master,name='master'),

    # url(r'^updatecourse/(?P<coursedata>\d+)/$', courseview.updatecourse, name='updatecourse'),
    # path('editstudent/<sno>', student.editstudent, name='editstudent'),
    # url('saverecord',views.saverecord,name='saverecord'),
    # url('storeprocedureuse',views.storeprocedureuse,name='storeprocedureuse'),
    # url('upload_excel',excelimportviews.upload_excel,name='upload_excel'),
  
]