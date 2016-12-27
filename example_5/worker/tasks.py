from celery import Celery
from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import chain

app = Celery('tasks', broker='redis://redis//')

@app.task()
def get_categories_task(term):
    print(term)
    return term
