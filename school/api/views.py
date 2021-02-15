import pprint
from rest_framework.utils import json
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.viewsets import ModelViewSet

from school.models import Student, Profile, School, Klass
from .serializers import (
    StudentSerializer, ProfileSerializer, 
    SchoolSerializer, KlassSerializer
)

class KlassViewSet(ModelViewSet):
    queryset = Klass.objects.all()
    authentication_classes = []
    permission_classes = [permissions.AllowAny]
    serializer_class = KlassSerializer
 
    def create(self, request, *args, **kwargs):
        # CREATE # ----------------------------------------------------------
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        student = serializer.save()  # self.perform_create()

        # BUGFIX M2M DATA 
        if student:
            for obj in student:
                student.klass_student.add(obj)
        
        headers = self.get_success_headers(serializer.data)
        print(serializer.data)
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    def update(self, request, *args, **kwargs):
        request.data['student'] = [
            Student.objects.create(**student_dict).id for student_dict in request.data['student']
        ]
        pprint.pprint(request.data) 
        return super().update(request, *args, **kwargs)