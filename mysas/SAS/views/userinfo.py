from django.shortcuts import render
from SAS.models import UserInfo


def student(request):
    return render(request, "student.html")


def teacher(request):
    return render(request, "teacher.html")


def info_list(request):
    # get data using objects from db
    data_list = UserInfo.objects.all()

    return render(request, "info.html", {"data_list": data_list})

def changePassword(request):
    return render(request, "changePassword.html")

def viewAttendance(request):
    return render(request, "viewAttendance.html")

def bookSlot(request):
    return render(request, "bookSlot.html")

def teacherAttendance(request):
    return render(request, "teacherAttendance.html")

def teacherMark(request):
    return render(request, "teacherMark.html")
        

