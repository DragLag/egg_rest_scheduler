from rest_framework import serializers
from .models import CronEgg
from cron_validator.regexes import regex_list


class CronEggSerializer(serializers.ModelSerializer):
    class Meta:
        model = CronEgg
        fields = ('egg', 'cron_string')

    def validate_cron_string(self, value):
        """
        check if a string is a right cron format
        """
        parts = value.split(' ')
        if len(parts) != 5:
            raise serializers.ValidationError('invalid expression')
        elements = list()
        for i in range(0, 5):
            m = regex_list[i].fullmatch(parts[i])
            if not m:
                raise serializers.ValidationError('one or more cron element are not valid')
        return value