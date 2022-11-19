from django.shortcuts import render, HttpResponse, redirect
from django import forms
from io import BytesIO

from SAS.models import UserInfo
from SAS.utils.bootstrap import BootStrapForm
from SAS.utils.encrypt import md5


class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="username",
        widget=forms.TextInput,
        required=True
    )
    password = forms.CharField(
        label="password",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )

    # def clean_password(self):
    #     pwd = self.cleaned_data.get("password")
    #     return md5(pwd)


def login(request):
    """ 登录 """
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # print(form.cleaned_data)
        # 验证成功，获取到的用户名和密码
        # {'username': 'wupeiqi', 'password': '123',"code":123}
        # {'username': 'wupeiqi', 'password': '5e5c3bad7eb35cba3638e145c830c35f',"code":xxx}

        # 去数据库校验用户名和密码是否正确，获取用户对象、None
        # admin_object = models.Admin.objects.filter(username=xxx, password=xxx).first()
        admin_object = UserInfo.objects.filter(**form.cleaned_data).first()

        # print(accounttype)
        if not admin_object:
            form.add_error("password", "wrong user name or password")
            # form.add_error("username", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

        # print(admin_object.accounttype)
        if admin_object.accounttype == "student":
            return redirect("/student/")

        # # 用户名和密码正确
        # # 网站生成随机字符串; 写到用户浏览器的cookie中；在写入到session中；
        # request.session["info"] = {'id': admin_object.id, 'name': admin_object.username}
        # # session可以保存7天
        # request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/teacher/")

    return render(request, 'login.html', {'form': form})


def logout(request):
    """ 注销 """

    request.session.clear()

    return redirect('/login/')
