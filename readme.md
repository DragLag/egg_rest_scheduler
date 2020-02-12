Egg api scheduler

Run and schedule eggs with api.

the egg have to runnable and a __main__.py file have to be included:

  __main__.py
├───EGG-INFO
└───project_dir
 
 the content of the __main__.py looks like:
 
from project_dir.dir import run

run()

the run() method is the execution method for the egg.



to run the application:

python manage.py runserver

to execute the schuduler tasks

python manage.py process_tasks --queue scheduler

to execute the jobs

python manage.py process_tasks --queue jobs


the api are documented on localhost:8000/docs/