from rest_framework import serializers
from uploadapp.models import File
from background_task.models import Task
from background_task.models_completed import CompletedTask


class ViewerFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file_name', 'version', 'file', 'pub_date')


class RunEggSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ['file_name']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('id', 'task_name', 'run_at', 'last_error')
        fields = '__all__'

class CompletedTaskdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedTask
        #fields = ('id', 'task_name', 'run_at', 'last_error')
        fields = '__all__'

