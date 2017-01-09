from celery import Celery
from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import chain
import wiki
import redis

app = Celery('tasks', broker='redis://redis//')
r = redis.Redis(host='redis')

@app.task()
def is_term_in_category(term, rootCategory):
    categories = wiki.categorize_term(term)

    lazy_chain = chain(
        validate_category_task.s(term, category, i, len(categories), rootCategory) for i, category in enumerate(categories)#cat in categories
    )
    res = lazy_chain(False)

@app.task()
def validate_category_task(lastResult, term, category, index, count, rootCategory):
    if not lastResult:
        print('validating term: {0} of category: {1} in root: {2}'.format(term, category, rootCategory))
        result = wiki.is_category_child_of_root(term, category, rootCategory)
        print('result of term: {0} of category: {1} in root: {2} is {3}'.format(term, category, rootCategory, result))
        print('index: {0}, count: {1}'.format(index, count))
        if result or index == count - 1:            
            r.hset('terms:' + term, 'term', term)
            r.hset('terms:' + term, 'root', rootCategory)
            r.hset('terms:' + term, 'valid', result)
            print("end of line")

        return result
    print("end of line - lastResut was true")
    return lastResult