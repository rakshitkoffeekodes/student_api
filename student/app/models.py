from django.db import models


# Create your models here.

class student(models.Model):
    student_name = models.CharField(max_length=30)
    student_father_name = models.CharField(max_length=30)
    student_mother_name = models.CharField(max_length=30)
    student_dob = models.DateField()