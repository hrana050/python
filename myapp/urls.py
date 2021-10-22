
from django.conf.urls import url
from django.urls import path
from django.urls.conf import include
from . import views
from . import loginviews, student, courseview,examview
from . import excelimportviews



urlpatterns=[

  # path('',views.master),
    path('',views.home,name='home'),
    path('about',views.about,name='about'),
    path('adminlogin',loginviews.login,name='adminlogin'),
    path('studentlogin',loginviews.studentlogin,name='studentlogin'),
    path('logout',loginviews.logout,name='logout'),
    path('studentlogout',loginviews.studentlogout,name='studentlogout'),
    path('dashboard', loginviews.dashboard, name='dashboard'),
    path('studentdashboard', loginviews.studentdashboard, name='studentdashboard'),
    path('addcourse', courseview.addcourse, name='addcourse'),
    url(r'^deletecourse/(?P<sno>\d+)/$', courseview.deletecourse, name='deletecourse'),
    url(r'^editcourse/(?P<sno>\d+)/$', courseview.editcourse, name='editcourse'),
    url('updatecourse', courseview.updatecourse, name='updatecourse'),
    path('addstudent', student.addstudent, name='addstudent'),
    path('studentlist', student.studentlist, name='studentlist'),
    url(r'^editstudent/(?P<sno>\d+)/$', student.editstudent, name='editstudent'),
    url('update', student.update, name='update'),
    #path('update/<int:id>', student.update, name='update'),
    path('edit/<sno>', student.edit, name='edit'),
    url('cancel', student.cancel, name='cancel'), 
    url(r'^deletestudent/(?P<sno>\d+)/$', student.deletestudent, name='deletestudent'), 
    path('',views.master,name='master'),
    path('uploadimage', views.home_view),
    path('addexamsetup', examview.addexamset, name='addexamsetup'),
    path('addcoursetype', courseview.addcoursetype, name='addcoursetype'),
    url(r'^editcoursetype/(?P<sno>\d+)/$', courseview.editcoursetype, name='editcoursetype'),
    url('updatecoursetype', courseview.updatecoursetype, name='updatecoursetype'),



    # url(r'^updatecourse/(?P<coursedata>\d+)/$', courseview.updatecourse, name='updatecourse'),
    # path('editstudent/<sno>', student.editstudent, name='editstudent'),
    # url('saverecord',views.saverecord,name='saverecord'),
    url('storeprocedureuse',views.storeprocedureuse,name='storeprocedureuse'),
    # url('upload_excel',excelimportviews.upload_excel,name='upload_excel'),
  
]