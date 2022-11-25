from django.shortcuts import render, redirect
from django import forms

from SAS import models
from SAS.models import UserInfo, Attendance


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["password", "cpassword"]


def student(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')


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
    if request.method == "GET":
        form = UserModelForm()
        return render(request, "changePassword.html", {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        newpwd = form.cleaned_data.get("password")
        cpwd = form.cleaned_data.get("cpassword")
        if newpwd == cpwd:
            UserInfo.objects.filter(studentID=studentid).update(password=newpwd)
            UserInfo.objects.filter(studentID=studentid).update(cpassword=cpwd)
            return redirect('/logout/')
        form.add_error("cpassword", "password and cpassword doesn't equal")
        return render(request, "changePassword.html", {"form": form})
    return render(request, "changePassword.html", {"form": form})


def viewAttendance(request):
    # stud = UserInfo.objects.get(id)
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_object = UserInfo.objects.filter(studentID=studentid).first()
    return render(request, "viewAttendance.html", {"obj": attend_object})


def bookSlot(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    attend_object = UserInfo.objects.filter(studentID=studentid).first()

    return render(request, "bookSlot.html", {"obj": attend_object})


def teacherAttendance(request):
    # context = {}
    all_att = UserInfo.objects.all()
    # context["attendance"] = all_att
    return render(request, "teacherAttendance.html", {"objs": all_att})


def teacherMark(request):
    return render(request, "teacherMark.html")


def correctAttendance(request):
    all_att = UserInfo.objects.all()
    return render(request, "correctAttendance.html", {"objs": all_att})
