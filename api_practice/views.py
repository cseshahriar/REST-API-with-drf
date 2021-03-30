from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .serializers import EmployeeSerializer, QuestionSerializer
from .models import Question

""" ========================= function base views =========================="""
@csrf_exempt
def question_list_create(request):

    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400) # bad request

@csrf_exempt
def question_detail_update(request, id):

    try:
        instance = Question.objects.get(id=id)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Object not found!"}, status=404)

    if request.method == 'GET':
        serializer = QuestionSerializer(instance)
        return JsonResponse(serializer.data, status=200)

    if request.method == 'PUT':
        json_parser = JSONParser()
        data = json_parser.parse(request)
        serializer = QuestionSerializer(instance=instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=202)
        return JsonResponse(serializer.errors, status=400) # bad request

    if request.method == 'DELETE':
        instance.delete()
        return HttpResponse(status=204)



""" ========================= viewsets =========================="""
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
