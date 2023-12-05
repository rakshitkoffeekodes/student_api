from django.db import models


# Create your models here.


# class Document(models.Model):
#     upload_document = models.FileField(upload_to='files/')


class student(models.Model):
    student_name = models.CharField(max_length=30)
    student_father_name = models.CharField(max_length=30)
    student_mother_name = models.CharField(max_length=30)
    student_dob = models.DateField()
    upload_document = models.JSONField()
    datetime = models.DateTimeField()

    def __str__(self):
        return self.student_name


class ParentsData(models.Model):
    student = models.ForeignKey(student, on_delete=models.CASCADE)
    parents_name = models.CharField(max_length=30)
    parents_mobile_no = models.CharField(max_length=10, unique=True)
    parents_email = models.EmailField(unique=True)
    parents_gender = models.CharField(max_length=20)
    parents_DOB = models.DateField()

    def __str__(self):
        return self.parents_name
