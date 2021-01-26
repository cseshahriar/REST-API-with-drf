from django.urls import path
from . views import employeeView

urlpatterns = [
    path('employee/', employeeView, name='employee'),
]