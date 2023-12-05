from rest_framework import serializers
from .models import *


class studentserilizer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = (
        'student_name', 'student_father_name', 'student_mother_name', 'student_dob', 'upload_document', 'datetime')


class ParentsDataserilizer(serializers.ModelSerializer):
    class Meta:
        model = ParentsData
        fields = ('student_name', 'parents_name', 'parents_mobile_no', 'parents_email', 'parents_gender', 'parents_DOB')
