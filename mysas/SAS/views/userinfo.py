from django.shortcuts import render,redirect
from SAS.models import UserInfo, Attendance
from SAS.views import account


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


def viewAttendance(request):
    # stud = UserInfo.objects.get(id)
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_object = UserInfo.objects.filter(studentID=studentid).first()


    # context = {}
    # all_att = Attendance.objects.all()
    # # all = []
    # context["attendance"] = all_att
    # a = AttendanceTotal()#tried to add after attendance calculation but needs more work
    # a.save()
    # all.append(a)
    return render(request, "viewAttendance.html", {"obj": attend_object})


def bookSlot(request):
    return render(request, "bookSlot.html")


def teacherAttendance(request):
    return render(request, "teacherAttendance.html")


def teacherMark(request):
    return render(request, "teacherMark.html")
        

