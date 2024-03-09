from django.db import models



# Create your models here.
class StudentInfo(models.Model):
    studentName=models.CharField(max_length=50)
    studentBranch=models.CharField(max_length=50)
    studentEmail=models.CharField(max_length=50)
    studentSemester=models.CharField(max_length=50)

    def __str__(self):
        return self.studentName
