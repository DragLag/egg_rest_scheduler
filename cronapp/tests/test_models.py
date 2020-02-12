from django.test import TestCase
from cronapp.models import CronEgg
from uploadapp.models import File
import unittest

# Create your tests here.

class CETestCase(TestCase):
    def setUp(self):
        egg = File.objects.create(file_name='file_name',
                                  version='0.1',
                                  file='test_file.txt')
        print(egg)
        CronEgg.objects.create(egg=egg, cron_string="******")

    def test_get_all(self):
        res = CronEgg.objects.all()
        print(res)
        assert res


