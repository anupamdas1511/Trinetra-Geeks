from flask import Flask,render_template,request,flash,session,redirect
import json
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import smtplib


# config file
with open('config.json','rt') as f:
    config=f.read()

params = json.loads(config)["params"]

app=Flask(__name__)
app.secret_key = 'trinetra-geeks'


#extensions
@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    if (request.method == 'POST'):
        username = request.form.get('name')
        userpass = request.form.get('pass')
        if username in params['admin_users']:
            admin_index = params['admin_users'].index(username)
            print("done")
        if (username in params['admin_users'] and userpass == params['admin_passwords'][admin_index]):
            # set the session variable
            print('done')
            session['user'] = username
            print("session done")
        else:
            return redirect("/login")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if (session['user'] in params['admin_users']):
        return "dashboard"
    else:
        return redirect("/login")


# listening
app.run(debug=True)