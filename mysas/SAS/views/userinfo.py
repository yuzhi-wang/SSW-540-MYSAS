from django.shortcuts import render,redirect
from SAS.models import UserInfo, Attendance
from SAS.views import account

from django.contrib import messages


def student(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_object = UserInfo.objects.filter(studentID=studentid).first()
    # print(attend_object.username)

    return render(request, "student.html", {"id": studentid})


def teacher(request):
    return render(request, "teacher.html")


def info_list(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_object = UserInfo.objects.filter(studentID=studentid).first()

    return render(request, "info.html", {"data_obj": attend_object})


def changePassword(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_object = UserInfo.objects.filter(studentID=studentid).first()

    return render(request, "changePassword.html")

def savePassword(request):
    message='are bc!!'
    if request.method=="POST":
        newpwd=request.POST.get("password")
        pwd=UserInfo(password=newpwd)
        pwd.save()
        message='Password updated Successfully'

    return render(request, "changePassword.html",{'message':message})

'''
def savePassword(request,id):
    message='are bc!!'
    updatepass=UserInfo.objects.get(id=id)
    stud=UserInfo(request.POST, instance=updatepass)
    if stud.is_valid:
        stud.save()
        messages.success(request,"Updated")
        return render(request,"changePassword.html",{"UserInfo":updatepass})
'''
    


def viewAttendance(request):
    # stud = UserInfo.objects.get(id)
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_object = UserInfo.objects.filter(studentID=studentid).first()
    #form=studpass

    # context = {}
    # all_att = Attendance.objects.all()
    # # all = []
    # context["attendance"] = all_att
    # a = AttendanceTotal()#tried to add after attendance calculation but needs more work
    # a.save()
    # all.append(a)
    return render(request, "viewAttendance.html", {"obj": attend_object})


def bookSlot(request):
   studentid = request.session.get('info')
   if not studentid:
        return redirect('/login/')
   attend_object = UserInfo.objects.filter(studentID=studentid).first()

   return render(request, "bookSlot.html",{"obj":attend_object})


def teacherAttendance(request):
    #context = {}
    all_att = UserInfo.objects.all()
    #context["attendance"] = all_att
    return render(request, "teacherAttendance.html",{"objs":all_att})


def teacherMark(request):
    return render(request, "teacherMark.html")

def correctAttendance(request):
    all_att = UserInfo.objects.all()
    return render(request, "correctAttendance.html",{"objs":all_att})    
        

