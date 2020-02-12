from django.urls import path
from .views import *


urlpatterns = [
    path('', FileUploadView.as_view()),
    path('<int:pk>/', FileUploadView.as_view()),
]