"""
URL configuration for tr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import imp
from django.contrib import admin
from django.urls import path
from userapp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',loginpage,name="loginpage"),
    path('signup/',signup,name="signup"),
    path('dashboard',dashboard,name="dashboard"),
    path('create_student/',create_student,name="create_student"),
    path('students_list/',students_list,name="students_list"),
    path('delete_student/<int:pid>',delete_student,name="delete_student"),
    path('edit_student/<int:pid>',edit_student,name="edit_student"),
    path('attendece/',attendence,name='attendence'),
    path('reg_attendence/<int:pid>',reg_attendence,name="reg_attendence"),
    path('reg_apsent/<int:pid>',reg_apsent,name="reg_apsent"),
    path('signout',signout,name="signout")
]

