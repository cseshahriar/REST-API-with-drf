from django.shortcuts import render
from rest_framework.response import Response
from . models import Student
from . serializers import StudentSerializer


def student_list(request):
    if request.method  == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)



