from .serializers import CronEggSerializer
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import CronEgg
from uploadapp.models import File
from cron_descriptor import get_description

import logging
logger = logging.getLogger('db')

class CronEggViewSet(viewsets.ViewSet):
    serializer_class = CronEggSerializer
    queryset = CronEgg.objects.all()

    def list(self, request):
        """
        Return all the scheduled cron_jobs
        """
        queryset = CronEgg.objects.all()
        serializer = CronEggSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        """
        Create a new cron_job:
        """
        data = JSONParser().parse(request)
        serializer = CronEggSerializer(data=data)
        egg = File.objects.get(id=data['egg'])
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            new_cron = CronEgg.objects.latest('id')
            response_text = {'cron_job_id': new_cron.id}
            logger.info("{} egg scheduled : {} ".format(data['egg'], get_description(data['cron_string'])))
            return JsonResponse(response_text, status=201, safe=True)
        else:
            response_text = {'error': serializer.errors}
            JsonResponse(response_text,status=400)
        return JsonResponse(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        """
        retrieve a cron_job given an cron_job id
        """
        queryset = CronEgg.objects.all()
        egg = get_object_or_404(queryset, pk=pk)
        serializer = CronEggSerializer(egg)
        return Response(serializer.data)

    def update(self, request, pk=None):
        """
        update a cron_job given a cron_job id
        """
        data = JSONParser().parse(request)
        egg = CronEgg.objects.get(pk=pk)
        if egg:
            egg.cron_string = data['cron_string']
            egg.save()
            response_text = {'cron_job_id': egg.id}
            logger.info("{} egg trigger updated : {} ".format(data['egg'], get_description(data['cron_string'])))
            return JsonResponse(response_text, status=201, safe=True)
        response_text = {'message': 'trigger was not updated'}
        return JsonResponse(response_text, status=400, safe = True)


    def destroy(self, request, pk=None):
        """
        delete a cron_job given a cron_job id
        """
        egg = CronEgg.objects.get(pk=pk)
        if egg:
            egg.delete()
            response_text = {'message': 'trigger deleted correctly'}
            logger.info(" trigger {} deleted ".format(pk))
            return JsonResponse(response_text, status=201, safe=True)
        response_text = {'message': 'trigger does not exists'}
        return JsonResponse(response_text, status=400, safe=True)
