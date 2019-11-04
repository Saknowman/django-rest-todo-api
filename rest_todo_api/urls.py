from rest_framework import routers
from .views import TodoTaskViewSet, TodoTaskStatusViewSet, TodoTaskTagViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TodoTaskViewSet)
router.register(r'status', TodoTaskStatusViewSet)
router.register(r'tags', TodoTaskTagViewSet)
