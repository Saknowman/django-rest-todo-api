from rest_framework import viewsets

from .models import TodoTask, TodoTaskStatus, TodoTaskTag
from .serializers import TodoTaskSerializer, TodoTaskStatusSerializer, TodoTaskTagSerializer

class TodoTaskViewSet(viewsets.ModelViewSet):
    queryset = TodoTask.objects.all()
    serializer_class = TodoTaskSerializer
    filter_fields = ('title', 'created_by', 'tag', 'status', 'completed')

class TodoTaskStatusViewSet(viewsets.ModelViewSet):
    queryset = TodoTaskStatus.objects.all()
    serializer_class = TodoTaskStatusSerializer

class TodoTaskTagViewSet(viewsets.ModelViewSet):
    queryset = TodoTaskTag.objects.all()
    serializer_class = TodoTaskTagSerializer
