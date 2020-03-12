from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EggsViewSet, TasksViewSet, TaskCompletedViewSet

router = DefaultRouter()
router.register(r'', EggsViewSet)
router.register(r'task', TasksViewSet)
router.register(r'taskscompleted', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]