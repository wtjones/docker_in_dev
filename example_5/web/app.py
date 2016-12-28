from flask import Flask, render_template, request, redirect, url_for
from celery import Celery
import redis
import os

app = Flask(__name__)
r = redis.Redis(host='redis')
celery = Celery('tasks', broker='redis://redis//')

@app.route("/")
def index():
    termsViewData = []

    for key in r.keys('terms:*'):
        rawTerm = r.hgetall(key)
        valid = 'True' if b'valid' in rawTerm and rawTerm[b'valid'].decode('UTF-8') == "True" else False
        newItem = {
            'term': rawTerm[b'term'].decode('UTF-8'),
            'root': rawTerm[b'root'].decode('UTF-8'),
            'valid': valid
        }
        
        termsViewData.append(newItem)
        
    return render_template(
        'index.html',
        message='See if a thing is in a wikipedia category.',
        terms=termsViewData,
        deploy_mode=os.environ['DEPLOY_MODE'])

@app.route('/categorize', methods=['POST'])
def categorize():
    term = request.form['term']
    root = request.form['root']
    
    print ('calling task for term: {0}, root {1}'.format(term, root))
    celery.send_task('tasks.is_term_in_category', ([term, root]))
    return redirect(url_for('index'))