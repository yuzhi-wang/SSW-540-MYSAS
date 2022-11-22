from django.db import models

# Create your models here.


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    accounttype = models.CharField(max_length=16)
    classname = models.CharField(max_length=32, default='ELC')
    totalclass = models.IntegerField(default=10)
    attnumber = models.IntegerField(default=0)
    studentID = models.CharField(max_length=32, default='000')


# class Department(models.Model):
#     title = models.CharField(max_length=16)


class Attendance(models.Model):
    studentID = models.CharField(max_length=32)
    attnumber = models.IntegerField(default=0)
    batch = models.CharField(max_length=32, default="ELC")
    totalclass = models.IntegerField(default=10)
    attendancepercentage = models.IntegerField(default=0)
    classtoattend = models.IntegerField(default=10)
    

#tried to calculate but needs more work#not used any were
# class AttendanceTotal(models.Model):
#     UserInfo = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
#     @property
#     def attendance_percentage(self):
#         attendedclass = Attendance.objects.get(num=self.attendancenumber)
#         totalclass = 10
#         attendance = round(attendedclass/totalclass *100,2)
#         return attendance
#
#     @property
#     def class_to_attend(self):
#         attendedclass = Attendance.objects.get(num=self.attendancenumber)
#         totalclass = 10
#         classtoattend = totalclass - attendedclass
#         return classtoattend
# use class.object.create to insert new sql values

# UserInfo.objects.create(username="yuzhi", password="123456", accounttype="teacher")
#Attendance.objects.create(studentID="sush",attandancenumber=6,batch="ELC091A",totalclass=10,attendancepercentage=50,classtoattend=4 )
