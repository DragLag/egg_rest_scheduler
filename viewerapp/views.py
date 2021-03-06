from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action
from rest_framework import viewsets
from .serializers import ViewerFileSerializer, RunEggSerializer, TaskSerializer, CompletedTaskdSerializer
from .tasks import run_egg, scheduled_egg
from django.conf import settings
import os
from background_task.models import Task
from background_task.models_completed import CompletedTask
from uploadapp.models import File

import logging
logger = logging.getLogger('db')

class EggsViewSet(viewsets.ViewSet):
    queryset = File.objects.all()
    serializer_class = ViewerFileSerializer()

    def list(self, request):
        """
        list all the uploaded eggs
        """
        queryset = File.objects.all()
        serializer = ViewerFileSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['POST'])
    def run(self, request):
        """
        Execeute an egg
        """
        data = JSONParser().parse(request)
        print(data)
        serializer = RunEggSerializer(data=data)
        if serializer.is_valid():
            exec_path = os.path.join(settings.MEDIA_ROOT, serializer.data['file_name'])
            run_egg(exec_path)
            logger.info(data['file_name'] + " executed per rest")
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

scheduled_egg(repeat = 60)

class TasksViewSet(viewsets.ViewSet):
    """
    retrieve:
    List all the uploaded eggs .
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer()

    def list(self, request):
        """
        List all the executed jobs
        """
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

class TaskCompletedViewSet(viewsets.ViewSet):
    """
    retrieve:
    List all the uploaded eggs .
    """
    queryset = CompletedTask.objects.all()
    serializer_class = CompletedTaskdSerializer()

    def list(self, request):
        """
        List all the completed executed jobs
        """
        queryset = Task.objects.all()
        serializer = CompletedTaskdSerializer(queryset, many=True)
        return Response(serializer.data)
