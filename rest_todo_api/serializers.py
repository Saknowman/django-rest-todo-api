from django.conf import settings
from rest_framework import serializers
from .models import TodoTask, TodoTaskStatus, TodoTaskTag
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=100, read_only=True)

class TodoTaskStatusSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoTaskStatus
    fields = ('pk', 'value')
    read_only_fields = ('pk',)

class TodoTaskTagSerializer(serializers.ModelSerializer):
  class Meta:
    model = TodoTaskTag
    fields = ('pk', 'value')
    read_only_fields = ('pk',)

class TodoTaskSerializer(serializers.ModelSerializer):
  status = TodoTaskStatusSerializer()
  tag = TodoTaskTagSerializer()
  created_by = UserSerializer()
  class Meta:
    model = TodoTask
    fields = ('pk', 'title', 'detail', 'due_date', 'status', 'tag', 'created_date', 'completed', 'completed_date', 'created_by')
    read_only_fields = ('pk', 'created_date', 'created_by',)
