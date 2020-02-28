import os
import logging
from multiprocessing import Process
from django.core.management import execute_from_command_line
logger = logging.getLogger(__name__)


def call_command(*args):
    logger.info("running commmand:" + " ".join(str(v) for v in args))
    execute_from_command_line(*args)


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weggcron.settings")
    args_server = ['name', 'runserver', '0.0.0.0:8000']
    args_scheduler = ['name', 'process_tasks', '--queue', 'scheduler']
    args_jobs = ['name', 'process_tasks', '--queue', 'jobs']
    django_server = Process(target=call_command, args=(args_server,))
    scheduler = Process(target=call_command, args=(args_jobs,))
    jobs = Process(target=call_command, args=(args_jobs,))
    django_server.start()
    scheduler.start()
    jobs.start()

