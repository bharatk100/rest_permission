from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    # owner=models.ForeignKey('auth.User',related_name='tasks')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


