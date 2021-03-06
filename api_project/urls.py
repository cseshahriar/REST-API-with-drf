"""api_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/firstapp/', include('firstapp.urls')),
    # path('api/students/', include('students.urls')),
    path('api/', include('school.api.urls')),
    path('api/', include('cbvstudents.urls')),
    path('api/', include('nestedapp.urls')),
    path('api/polls/', include('pollsapi.api_urls')),
    path('api/', include('flight_reservations.urls')),
    path('api/token-auth/', views.obtain_auth_token),


    # api_practice
    path('api/api_practice/', include('api_practice.api_urls')),
]
