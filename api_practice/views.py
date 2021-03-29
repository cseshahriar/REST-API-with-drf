from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import EmployeeSerializer


from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, DjangoModelPermissions

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset  = User.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]