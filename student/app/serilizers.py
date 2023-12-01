from rest_framework import serializers
from .models import *


class studentserilizer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('student_name', 'student_father_name', 'student_mother_name', 'student_dob', 'upload_document')

# class Documentserilizer(serializers.ModelSerializer):
#     class Meta:
#         model = Document
#         fields = '__all__'
