from django.shortcuts import render
from django.http import JsonResponse
from .serilizers import *
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['POST'])
def add_student(request):
    student_name = request.POST['student_name']
    student_father_name = request.POST['student_father_name']
    student_mother_name = request.POST['student_mother_name']
    student_dob = request.POST['student_dob']
    try:
        student.objects.create(
            student_name=student_name,
            student_father_name=student_father_name,
            student_mother_name=student_mother_name,
            student_dob=student_dob
        )
        return JsonResponse({'status': 'add student'})
    except Exception as e:
        return JsonResponse({"status": e.__str__()})


@api_view(['GET'])
def view_student(request):
    stu = student.objects.all()
    serializer = studentserilizer(stu, many=True)
    return JsonResponse({'status': serializer.data})


@api_view(['POST'])
def update_student(request):
    try:
        pk = request.POST['id']
        student_name = request.POST['student_name']
        student_father_name = request.POST['student_father_name']
        student_mother_name = request.POST['student_mother_name']
        student_dob = request.POST['student_dob']
        up = student.objects.get(id=pk)
        if not student_name == '':
            up.student_name = student_name

        elif not student_father_name == '':
            up.student_father_name = student_father_name

        elif not student_mother_name == '':
            up.student_mother_name = student_mother_name

        elif not student_dob == '':
            up.student_dob = student_dob

        return JsonResponse({'status': 'update success',
                             'data': {'student_name': up.student_name, 'student_father_name': up.student_father_name,
                                      'student_mother_name': up.student_mother_name, 'student_dob': up.student_dob}})

    except Exception as e:
        return JsonResponse({'status': e.__str__()})


@api_view(['GET'])
def delete_student(request, pk):
    dlt = student.objects.get(id=pk)
    dlt.delete()
    dlt.save()
    return JsonResponse({'status': 'Delete successfully'})
