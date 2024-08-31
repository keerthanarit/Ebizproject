from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('adminhome', views.adminhome, name='adminhome'),
    path('userhome', views.userhome, name='userhome'),
    path('adminviewuserlist', views.adminviewuserlist, name='adminviewuserlist'),
    path('admindeleteuser', views.admindeleteuser, name='admindeleteuser'),
    path('adminaddservicecategory', views.adminaddservicecategory, name='adminaddservicecategory'),
   # path('admindeletecategory', views.admindeletecategory, name='admindeletecategory'),
    path('adminaddplans', views.adminaddplans, name='adminaddplans'),
    path('userviewprofile', views.userviewprofile, name='userviewprofile'),
    path('useraddservices', views.useraddservices, name='useraddservices'),
    path('useraddadvertisement', views.useraddadvertisement, name='useraddadvertisement'),
    path('useraddjobs', views.useraddjobs, name='useraddjobs'),

]
