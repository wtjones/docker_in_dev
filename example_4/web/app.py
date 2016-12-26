from flask import Flask, render_template, request, redirect, url_for
import redis
import os

app = Flask(__name__)

r = redis.Redis(host='redis')

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
    return redirect(url_for('index'))