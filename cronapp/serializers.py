from rest_framework import serializers
from .models import CronEgg


class CronEggSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronEgg
        fields = ('egg', 'cron_string')


