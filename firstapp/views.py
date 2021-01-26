from django.shortcuts import render
from django.http import JsonResponse
from . models import Employee

def employeeView(request):
    data = Employee.objects.all()
    response = {
        'employees': list(data.values('id','name', 'salary'))
    }
    return JsonResponse(response)