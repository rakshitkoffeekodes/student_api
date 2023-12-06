import datetime
import os
from django.core.files.storage import default_storage
from django.http import JsonResponse
from student import settings
from .serilizers import *
from .models import *
from rest_framework.decorators import api_view


# Create your views here.


@api_view(['POST'])
def add_student(request):
    student_name = request.POST['student_name']
    student_father_name = request.POST['student_father_name']
    student_mother_name = request.POST['student_mother_name']
    student_dob = request.POST['student_dob']
    upload_document = request.FILES.getlist('upload_document')
    try:
        data = Student()
        data.student_name = student_name
        data.student_father_name = student_father_name
        data.student_mother_name = student_mother_name
        data.student_dob = student_dob
        data.upload_document = [
            default_storage.save(os.path.join(settings.MEDIA_ROOT, 'document', file.name.replace(' ', '_')), file)
            for file in upload_document]
        data.datetime = datetime.datetime.now()
        data.save()
        return JsonResponse({'Massage': 'Success'})

    except Exception as e:
        return JsonResponse({'Massage': e.__str__()})


@api_view(['POST'])
def get_document(request):
    key = request.POST.get('id', '')
    if key != '':
        try:
            one_data = Student.objects.get(id=key)
            path = request.META['HTTP_HOST']
            path1 = ['http://' + path + '/media/' + one for one in one_data.upload_document]
            one_data.upload_document = path1
            print(path1)
            serial = studentserilizer(one_data)
            return JsonResponse({'Massage': 'Success', 'Data': serial.data})
        except Student.DoesNotExist:
            return JsonResponse({'Massage': 'ID is Not Exist.'})
        except Exception as e:
            return JsonResponse({'Massage': e.__str__()})

    else:
        student_data = Student.objects.all()
        serial = studentserilizer(student_data, many=True)
        return JsonResponse({'Massage': serial.data})


@api_view(['POST'])
def date_to_data(request):
    start_time = datetime.time(00, 00, 00)
    end_time = datetime.time(23, 59, 59)
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    try:
        start_object = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        start_datetime = datetime.datetime(year=start_object.year, month=start_object.month, day=start_object.day,
                                           hour=start_time.hour, minute=start_time.minute, second=start_time.second)
        end_object = datetime.datetime.strptime(end_date, "%Y-%m-%d")
        end_datetime = datetime.datetime(year=end_object.year, month=end_object.month, day=end_object.day,
                                         hour=end_time.hour, minute=end_time.minute, second=end_time.second)
        print(start_datetime, end_datetime)
        filter_data = Student.objects.filter(datetime__range=(start_datetime, end_datetime))
        serial = studentserilizer(filter_data, many=True)
        return JsonResponse({'Message': 'Success', 'Data': serial.data})
    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['POST'])
def parents(request):
    student_id = request.POST['student_id']
    parents_name = request.POST['parents_name']
    parents_mobile_no = request.POST['parents_mobile_no']
    parents_email = request.POST['parents_email']
    parents_gender = request.POST['parents_gender']
    parents_DOB = request.POST['parents_DOB']
    try:
        student_data = Student.objects.get(id=student_id)
        if student_data:
            data = Parents_data()
            data.student = student_data
            data.parents_name = parents_name
            data.parents_mobile_no = parents_mobile_no
            data.parents_email = parents_email
            data.parents_gender = parents_gender.lower()
            data.parents_DOB = parents_DOB
            data.save()

            return JsonResponse({'Message': 'Add Data'})
        else:
            return JsonResponse({'Message': 'Data is Not exist'})
    except Exception as e:
        return JsonResponse({'Message': e.__str__()})


@api_view(['GET'])
def view_student(request):
    data = Student.objects.all()
    serializer = studentserilizer(data, many=True)
    return JsonResponse({'Data': serializer.data})


@api_view(['POST'])
def update_student(request):
    primary_key = request.POST['id']
    update_one = Student.objects.get(id=primary_key)
    student_name = request.POST.get('student_name', '')
    student_father_name = request.POST.get('student_father_name', '')
    student_mother_name = request.POST.get('student_mother_name', '')
    student_dob = request.POST.get('student_dob', '')
    try:
        if not student_name == '':
            update_one.student_name = student_name

        if not student_father_name == '':
            update_one.student_father_name = student_father_name

        if not student_mother_name == '':
            update_one.student_mother_name = student_mother_name

        if not student_dob == '':
            update_one.student_dob = student_dob
        update_one.save()
        return JsonResponse({'Massage': 'update success',
                             'data': {'student_name': update_one.student_name,
                                      'student_father_name': update_one.student_father_name,
                                      'student_mother_name': update_one.student_mother_name,
                                      'student_dob': update_one.student_dob}})

    except Exception as e:
        return JsonResponse({'Massage': e.__str__()})


@api_view(['POST'])
def delete_student(request):
    primary_key = request.POST['id']
    delete_one = Student.objects.get(id=primary_key)
    delete_one.delete()
    return JsonResponse({'Massage': 'Delete successfully'})


