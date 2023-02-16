"""mysas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from SAS.views import account, userinfo, record

urlpatterns = [
    # path('index/', account.index),
    # front page
    path('', account.login),

    # user login
    path('login/', account.login),
    path('logout/', account.logout),
    # student info present
    path('info/', userinfo.info_list),
    # function for student
    path('viewAttendance/', userinfo.viewAttendance),
    path('bookSlot/', record.bookSlot),
    path('cancelSlot/', record.cancel_slot),
    path('changePassword/', userinfo.changePassword),
    # functions for teacher
    path('teacher/', record.teacher),
    path('teacherAttendance/', record.teacherAttendance),

    

    # test
    path('student/', userinfo.student),
    path('layout/', account.layout)
    # path('test/', userinfo.user_test)
]
