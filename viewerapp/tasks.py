import subprocess
from background_task import background
from cronapp.models import CronEgg
from uploadapp.models import File
from django.conf import settings
from croniter import croniter
from datetime import datetime
import os

@background(schedule = 5, queue = 'jobs')
def run_egg(egg):
    print("running egg {}".format(egg))
    subprocess.call(["python", egg])

@background(schedule= 5, queue = 'scheduler')
def scheduled_egg():
    egg_set = CronEgg.objects.all()
    for egg in egg_set:
        base = datetime.now()
        iter = croniter(egg.cron_string, base)
        prev = str(iter.get_prev(datetime).strftime("%Y%m%d%H%M"))
        now = str(datetime.now().strftime("%Y%m%d%H%M"))
        if prev == now:
            egg_to_run = File.objects.get(id = egg.egg_id)
            print("egg {}, version {}, scheduled at time {}".format(egg_to_run.file_name, egg_to_run.version, datetime.now()))
            exec_path = os.path.join(settings.MEDIA_ROOT, egg_to_run.file_name)
            run_egg(exec_path)
