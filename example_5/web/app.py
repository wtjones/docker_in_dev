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
        message="Please register!",
        users=users,
        deploy_mode=os.environ['DEPLOY_MODE'])

@app.route('/register', methods=['POST'])
def register():
    user = request.form['user']
    r.sadd('users', user)
    print ('adding user: {0}'.format(user))
    celery.send_task('tasks.get_categories_task', ([user]))
    return redirect(url_for('index'))