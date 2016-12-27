from flask import Flask, render_template, request, redirect, url_for
#from celery.execute import send_task
from celery import Celery
import redis
import os

app = Flask(__name__)

r = redis.Redis(host='redis')

celery = Celery('tasks', broker='redis://redis//')

@app.route("/")
def index():
    users = []
    
    # redis provides byte[], so convert to string
    for user in r.smembers('users'):
        users.append(user.decode('UTF-8'))

    return render_template(
        'index.html',
        message='See if a thing is under a category.',
        users=users,
        deploy_mode=os.environ['DEPLOY_MODE'])

@app.route('/categorize', methods=['POST'])
def categorize():
    term = request.form['term']
    root = request.form['root']
    print ('calling task for term: {0}'.format(term))
    celery.send_task('tasks.is_term_in_category', ([term, root]))
    return redirect(url_for('index'))