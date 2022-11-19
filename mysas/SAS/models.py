from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    accounttype = models.CharField(max_length=16)


class Department(models.Model):
    title = models.CharField(max_length=16)


class Attendance(models.Model):
    studentID = models.CharField(max_length=32)

# use class.object.create to insert new sql values

# UserInfo.objects.create(username="yuzhi", password="123456", accounttype="teacher")
