from django.shortcuts import render
from django.http import JsonResponse


def employeeView(request):
    employee = {
        'id': 123,
        'name': 'John',
        'sal': 20000
    }
    return JsonResponse(employee)