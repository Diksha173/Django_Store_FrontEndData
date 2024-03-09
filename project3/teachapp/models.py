from django.db import models

# Create your models here.
class TeacherInfo(models.Model):
    teacherName=models.CharField(max_length=50)
    teacherSubject=models.CharField(max_length=50)
    teacherEmail=models.CharField(max_length=50)