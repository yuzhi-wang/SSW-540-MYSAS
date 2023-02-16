from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Welcome")


def user_list(request):
    return render(request, "student.html")


def login(request):
    if request.method == "GET":
        return render(request, "login.html")
    else:
        # print(request.POST)
        username = request.POST.get("user")
        userpwd = request.POST.get("pwd")
        if username == "root" and userpwd == "123":
            return render(request, "student.html")
        else:
            # return HttpResponse("Fail")
            return render(request, "login.html", {"error_msg": "wrong password"})
