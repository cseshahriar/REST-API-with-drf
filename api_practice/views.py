from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from rest_framework.views import APIView
from rest_framework.response import Response

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



""" ========================= class base view =========================="""
class QuestionListCreateAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        data = request.data
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) # bad request


class QuestionDetailAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def get_object(self, id):
        try:
            return Question.objects.get(id=id)
        except Question.DoesNotExist as e:
            return Response({"error": "Object not found!"}, status=404)

    def get(self, request, id=None):
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance)
        return Response(serializer.data, status=200)

    def put(self, request, id=None):
        data = request.data
        instance = self.get_object(id)
        serializer = QuestionSerializer(instance, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=202)
        return Response(serializer.errors, status=400) # bad request

    def delete(self, request, id=None):
        self.get_object(id).delete()
        return HttpResponse(status=204)

""" ========================= viewsets =========================="""
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
