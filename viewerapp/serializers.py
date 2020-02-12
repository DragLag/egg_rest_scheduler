from rest_framework import serializers
from uploadapp.models import File
from background_task.models import Task


class ViewerFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file_name', 'version', 'file', 'pub_date')


class RunEggSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file_name']


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'task_name', 'run_at', 'last_error')
        fields = '__all__'
