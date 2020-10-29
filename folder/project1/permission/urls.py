from django.urls import path

from . import views

from .views import TaskList, TaskDetail

urlpatterns = [
        path('list/', TaskList.as_view(), name='list'),
        path('list/<str:pk>', TaskDetail.as_view(), name='detail'),
]