from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KlassViewSet

app_name = 'school'
router = DefaultRouter()
router.register('school', KlassViewSet)

urlpatterns = [
    path('', include(router.urls)),
]