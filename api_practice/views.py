from rest_framework import viewsets
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions

from .serializers import EmployeeSerializer, QuestionSerializer
from .models import Question

""" ========================= function base views =========================="""
def question_list_view(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return JsonResponse(serializer.data, safe=False)



""" ========================= viewsets =========================="""
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]
