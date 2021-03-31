from django.urls import path
from .views import PollList, PollDetail, UserCreate


from rest_framework.routers import DefaultRouter
from .views import PollViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("/", PollList.as_view(), name="polls_list"),
    path("/<int:pk>/", PollDetail.as_view(), name="polls_detail"),
    path("users/", UserCreate.as_view(), name="user_create"),
]
urlpatterns += router.urls
