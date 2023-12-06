from rest_framework import serializers
from .models import *


class studentserilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            'student_name', 'student_father_name', 'student_mother_name', 'student_dob', 'upload_document', 'datetime')


class Parentsserilizer(serializers.ModelSerializer):
    class Meta:
        model = Parents_data
        fields = ('student_name', 'parents_name', 'parents_mobile_no', 'parents_email', 'parents_gender', 'parents_DOB')
