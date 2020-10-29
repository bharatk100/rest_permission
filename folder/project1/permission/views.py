from django.shortcuts import render
from . serializers import TaskSerializer
from . models import Task

from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from . permission import IsOwnerorReadOnly
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class TaskMixin(object):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_class= (IsAuthenticated, IsOwnerorReadOnly,)

    def pre_save(self, obj):
        obj.owner= self.request.user


class TaskList(TaskMixin, ListCreateAPIView):
    pass


class TaskDetail(TaskMixin, RetrieveUpdateDestroyAPIView):
    pass