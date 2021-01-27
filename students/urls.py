from django.urls import path
from . views import (
    student_list_create_api_view,
    student_detail_update_delete_api_view
)

urlpatterns = [
    path('list_create/',
        student_list_create_api_view,
        name='student_list_create'
    ),
    path(
        'detail_update_delete/<int:pk>/',
        student_detail_update_delete_api_view,
        name='student_detail_update_delete'
    )
]