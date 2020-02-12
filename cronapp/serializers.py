from rest_framework import serializers
from .models import CronEgg
from cron_validator import CronValidator


class CronEggSerializer(serializers.ModelSerializer):
#class CronEggSerializer(serializers.Serializer):

    #egg = serializers.CharField(max_length=200)
    #cron_string = serializers.CharField()
    class Meta:
        model = CronEgg
        fields = ('egg', 'cron_string')


    def validate_cron_string(self, value):
        """
        check if a string is a right cron format
        """
        print(CronValidator.parse(value))
        if CronValidator.parse(value) is None:
            raise serializers.ValidationError('The cron string is not valid')
        return value