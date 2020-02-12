from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import EggsViewSet, TasksViewSet

router = DefaultRouter()
router.register(r'', EggsViewSet)
router.register(r'task', TasksViewSet)

urlpatterns = [
    path('', include(router.urls)),
]