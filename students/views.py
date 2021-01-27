from django.shortcuts import render
from rest_framework.response import Response
from . models import Student
from . serializers import StudentSerializer
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET', 'POST'])
def student_list_create_api_view(request):
    """ student list and create api view """
    if request.method  == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def student_detail_update_delete_api_view(request, pk):
    """ student detail api view """
    try:
        student_object = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student_object)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)        
    elif request.method = 'DELETE':
        student_object.delete()
        return Response(status=stats.HTTP_204_NO_CONTENT)



