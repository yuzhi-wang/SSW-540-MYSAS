from django.shortcuts import render, redirect
from django import forms

from SAS import models
from SAS.models import UserInfo


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ["password", "cpassword"]


def student(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    return render(request, "student.html")


def info_list(request):
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    account_object = UserInfo.objects.filter(studentID=studentid).first()

    return render(request, "info.html", {"data_obj": account_object})


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
    studentid = request.session.get('info')
    if not studentid:
        return redirect('/login/')
    account_object = UserInfo.objects.filter(studentID=studentid).first()
    return render(request, "viewAttendance.html", {"obj": account_object})






