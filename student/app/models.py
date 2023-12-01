from django.db import models
# Create your models here.


# class Document(models.Model):
#     upload_document = models.FileField(upload_to='files/')


class student(models.Model):
    student_name = models.CharField(max_length=30)
    student_father_name = models.CharField(max_length=30)
    student_mother_name = models.CharField(max_length=30)
    student_dob = models.DateField()
    upload_document = models.JSONField(default=list)

