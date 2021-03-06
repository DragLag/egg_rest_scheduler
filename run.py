import os
import logging
from multiprocessing import Process
from django.core.management import execute_from_command_line
logger = logging.getLogger('db')


def call_command(*args):
    message =  "running commmand:" + " ".join(str(v) for v in args)
    #print(message)
    logger.info(message)
    execute_from_command_line(*args)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weggcron.settings")
    args_server = ['name', 'runserver', '0.0.0.0:8000']
    args_scheduler = ['name', 'process_tasks', '--queue', 'scheduler']
    args_jobs = ['name', 'process_tasks', '--queue', 'jobs']
    django_server = Process(target=call_command, args=(args_server,))
    scheduler = Process(target=call_command, args=(args_scheduler,))
    jobs = Process(target=call_command, args=(args_jobs,))
    django_server.start()
    jobs.start()
    scheduler.start()


