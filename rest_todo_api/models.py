from django.db import models
from django.conf import settings
from django.utils import timezone


class TodoTaskTag(models.Model):
    value = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.value

class TodoTaskStatus(models.Model):
    value = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.value

class TodoTask(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(default='')
    due_date = models.DateField(blank=True, null=True)
    status = models.ForeignKey(to=TodoTaskStatus, related_name='todo_tasks', on_delete=models.PROTECT)
    tag = models.ForeignKey(to=TodoTaskTag, blank=True, null=True, related_name='todo_tasks', on_delete=models.PROTECT)
    created_date = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(blank=True, null=True)
    created_by = models.ForeignKey(to=settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{tag}/{title}:{status}".format(title=self.title, status=self.status, tag=self.tag)
