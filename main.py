from flask import Flask,render_template,request,flash,session,redirect
import json
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
import smtplib



# config file
with open('config.json','rt') as f:
    config=f.read()

params = json.loads(config)["params"]

# books file
with open('book.json',encoding="utf8") as f:
    books=f.read()

book = json.loads(books)["books"]
print(book['1']['author'])

app=Flask(__name__)
app.secret_key = 'trinetra-geeks'


#extensions
@app.route("/",methods=['GET','POST'])
def home():
    if 'user' in session:
        user = session['user']
    
    else:
        user = "login"
    return render_template("index.html",user = user,book = book)



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

            return redirect("/")
        else:
            flash("user not registered","error")
            print("user not registered")

    return render_template("login.html")



@app.route("/dashboard")
def dashboard():
    if 'user' in session:
        if (session['user'] in params['admin_users']):
            return render_template("dashboard.html",user = session['user'])
    else:
        flash("you need to login first","suggestion")
        print("you need to login first","suggestion")
        return redirect("/login")


@app.route("/signup",methods=['GET','POST'])
def signup():
    if (request.method == 'POST'):
        username = request.form.get('name')
        userpass = request.form.get('pass')
        userpass_confirm = request.form.get('conf_pass')
        if userpass == userpass_confirm:
            if username in params['admin_users']:
                admin_index = params['admin_users'].index(username)
                flash("Your username is already registered","alert")
                print("username already registerd")
                return render_template("signup.html")
            else:
                params['admin_users'].append(username)
                params['admin_passwords'].append(userpass)
                session['user'] = username
                print("session done")
                print("successful")
                return redirect("/")
        else:
            flash("your passwords doesn't match",)
            print("your pass doesn't match")
    return render_template("signup.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect("/")

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/book/<string:book_no>")
def books_func(book_no):
    book_required = book[book_no]
    return render_template("book.html",book = book_required)




# listening
app.run(debug=True)