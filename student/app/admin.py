from django.contrib import admin
from .models import *
from django.contrib.auth.models import User, Group


# Register your models here.
class Studentadmin(admin.ModelAdmin):
    list_display = (
        'id', 'student_name', 'student_father_name', 'student_mother_name', 'student_dob', 'upload_document',
        'datetime')


class Parentsadmin(admin.ModelAdmin):
    list_display = (
        'id', 'student', 'parents_name', 'parents_mobile_no', 'parents_email', 'parents_gender', 'parents_DOB')
    verbose_name = 'Parents'


admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Student, Studentadmin)
admin.site.register(Parents_data, Parentsadmin)
