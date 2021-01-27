from django.urls import path
from . views import StudentListCreateApiView, StudentDetailApiView

urlpatterns = [
    path('list/', StudentListCreateApiView.as_view(), name='cbvstudent_list_create'),
    path('detail/<int:pk>/', StudentDetailApiView.as_view(), name='cbvstudent_detail'),
]