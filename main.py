from flask import Flask,render_template,request,flash
import json
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import smtplib


# config file
# with open('config.json','rt') as f:
#     config=f.read()
#
# params = json.loads(config)["params"]

app=Flask(__name__)


#extensions
@app.route("/",methods=['GET','POST'])
def home():
    return render_template("index.html")

@app.route("/login",methods=['GET','POST'])
def login():
    return render_template("login.html")


# listening
app.run(debug=True)