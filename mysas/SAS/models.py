from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(verbose_name="username", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)
    accounttype = models.CharField(verbose_name="accounttype", max_length=16)
    classname = models.CharField(verbose_name="classname", max_length=32, default='ELC')
    totalclass = models.IntegerField(verbose_name="totalclass", default=10)
    attnumber = models.IntegerField(verbose_name="attendant class", default=0)
    studentID = models.CharField(verbose_name="studentID", max_length=32, default='000')
    cpassword = models.CharField(verbose_name="cpassword", max_length=64)

# class Department(models.Model):
#     title = models.CharField(max_length=16)


class Attendance(models.Model):
    studentID = models.CharField(verbose_name="studentID", max_length=32)
    classname = models.CharField(verbose_name="classname", max_length=32)
    date = models.DateField(verbose_name="date")
    starttime = models.IntegerField(verbose_name="startTime",
                                    validators=[MinValueValidator(9), MaxValueValidator(17)]
                                    )
    attendance = models.CharField(verbose_name="attendance", max_length=16)
    grade = models.IntegerField(verbose_name="grade",
                                validators=[MinValueValidator(0), MaxValueValidator(100)]
                                )

    

# UserInfo.objects.create(username="yuzhi", password="123456", accounttype="teacher")

