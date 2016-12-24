from flask import Flask, render_template, request, redirect, url_for
import redis
import os

app = Flask(__name__)

r = redis.Redis(host=os.environ['FLASKDEMOREDIS_PORT_6379_TCP_ADDR'])

@app.route("/")
def index():
    users = r.smembers('users')
    return render_template('index.html', message="Hello World!", users=users)

@app.route('/register', methods=['POST'])
def register():
    user = request.form['user']

    users.append(user)
    print (user)
    return redirect(url_for('index'))