from django.contrib import admin

# Register your models here.
from .models import TodoTask, TodoTaskStatus, TodoTaskTag

@admin.register(TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoTaskStatus)
class TodoTaskStatusAdmin(admin.ModelAdmin):
    pass

@admin.register(TodoTaskTag)
class TodoTaskTagAdmin(admin.ModelAdmin):
    pass