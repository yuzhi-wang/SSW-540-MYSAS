from django.shortcuts import render
from SAS.models import UserInfo, Attendance , AttendanceTotal


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
    #stud = UserInfo.objects.get(id)

    context = {}
    all = Attendance.objects.all()
    #all = []
    context["attendance"] = all
    #a = AttendanceTotal()#tried to add after attendance calculation but needs more work
    #a.save()
    #all.append(a)
    return render(request, "viewAttendance.html",context)

def bookSlot(request):
    return render(request, "bookSlot.html")

def teacherAttendance(request):
    return render(request, "teacherAttendance.html")

def teacherMark(request):
    return render(request, "teacherMark.html")
        

