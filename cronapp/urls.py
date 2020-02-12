from django.urls import path,include
from rest_framework.routers import DefaultRouter
from . import views



#router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()
router.register(r'', views.CronEggViewSet)

urlpatterns = [
    path('', include(router.urls)),
]