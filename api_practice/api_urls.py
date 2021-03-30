from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls), name='user_list'),

    # ======================= function base views =============================
    path('questions/', question_list_create),
    path('questions/<int:id>/', question_detail_update), 
]