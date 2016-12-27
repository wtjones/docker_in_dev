from celery import Celery
from celery.decorators import task
from celery.utils.log import get_task_logger
from celery import chain
import wiki

app = Celery('tasks', broker='redis://redis//')

@app.task()
def is_term_in_category(term, rootCategory):
    categories = wiki.categorize_term(term)

    lazy_chain = chain(
        validate_category_task.s(term, cat, rootCategory) for cat in categories
    )
    res = lazy_chain(False)


@app.task()
def validate_category_task(lastResult, term, category, rootCategory):
    if not lastResult:
        print('validating term: {0} of category: {1} in root: {2}'.format(term, category, rootCategory))
        result = wiki.is_category_child_of_root(term, category, rootCategory)
        print('result of term: {0} of category: {1} in root: {2} is {3}'.format(term, category, rootCategory, result))
        return result
    return lastResult