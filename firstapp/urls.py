from django.urls import path
from . views import employeeView

urlpatterns = [
    path('api/employee', employeeView, name='employee'),
]