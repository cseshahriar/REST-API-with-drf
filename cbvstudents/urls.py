from django.urls import path, include

from . views import StudentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

"""
http://localhost:8000/api/cbvstudents/students/
"""

# urlpatterns = [
#     # path('list/', StudentListCreateApiView.as_view(), name='cbvstudent_list_create'),
#     # path('detail/<int:pk>/', StudentDetailApiView.as_view(), name='cbvstudent_detail'),
# ]