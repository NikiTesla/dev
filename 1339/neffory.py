from flask import Flask, render_template, url_for, request, redirect, make_response, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import sqlite3


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pidors.db'
db = SQLAlchemy(app)


# creating models of data
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    message = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'Message {self.id}'


class Pidor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'Pidor {self.id}'


# setting session
@app.route("/login", methods=['POST', 'GET'])
def setsession():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        users = sqlite3.connect(f'instance/pidors.db').cursor().execute(f"SELECT * FROM User WHERE username='{username}'").fetchone()
        
        if username == "" or password == "":
            return render_template("login.html", error="Field is empty")
        elif not users:
            return render_template("login.html", error="Wrong username")
        elif users[1] == username and users[2] == password:
            session['username'] = request.form['username']
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Wrong passsword or something else")
    return render_template("login.html")


@app.route("/unsetsession")
def unsetsession():
    session.pop('username', None)
    return redirect("/login")


app.secret_key = 'SECRET'

@app.route("/iamtryinggo")
def trygo():
	return "You are trying Golang! It's cool"

# Main page of website
@app.route("/", methods=['POST', 'GET'])
def index():
    try:
        messages = Message.query.order_by(Message.id.desc()).limit(10).all()
    except Exception:
        messages = []

    if request.method == "POST":
        username = session['username']
        message = request.form['message']
        
        if message == "":
            return render_template("main.html", messages=messages, login=session['username'])

        message = Message(username=username, message=message)

        try:
            db.session.add(message)
            db.session.commit()
            return redirect('/')
        except:
            return "Error occured"
    else:
        try:
            return render_template("main.html", messages=messages, login=session['username'])
        except Exception:
            return redirect("/login")


# Page with all participant of neffors' community
@app.route("/pidors")
def pidors():
    pidors = Pidor.query.order_by(Pidor.id).all()
    try:
        return render_template("pidors.html", pidors=pidors, login=session['username'])
    except Exception:
        return redirect("/login")
        


# add neffor to the list
@app.route("/add_pidor", methods=['POST', 'GET'])
def add_pidor():
    if request.method == "POST":
        pidor_name = request.form['name']
        pidor_text = request.form['text']

        pidor = Pidor(name=pidor_name, text=pidor_text)
        
        try:
            db.session.add(pidor)
            db.session.commit()
            return redirect('/pidors')
        except:
            return "Error occured"
    else:
        try:
            return render_template("add_pidor.html", login=session['username'])
        except Exception:
            return redirect("/login")


# show one neffor with id ...
@app.route("/pidor/<int:id>")
def fact(id):
    print(f"selected {id} pidor")
    pidor = Pidor.query.get(id)
    try:
        return render_template("pidor.html", pidor=pidor, login=session['username'])
    except Exception:
        return redirect("/login")


# page of deleting of neffor. not a page actually
@app.route("/pidor/delete/<int:id>")
def delete(id):
    db.session.delete(Pidor.query.get(id))
    db.session.commit()
    pidors()
    return redirect("/")


# signup of neffor
@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == "POST":
        login = request.form['username']
        password = request.form['password']
        users = sqlite3.connect(f'instance/pidors.db').cursor().execute(f"SELECT * FROM User WHERE username='{login}'").fetchall()
        
        if login == "" or password == "":
            return render_template("login.html", error="Field is empty")
        elif not users:
            neffor = User(username=login, password=password)
        else:
            return render_template("signup.html", error="Already exists")
       
        try:
            db.session.add(neffor)
            db.session.commit()
            return redirect('/')
        except:
            return "Error occured"
    else:
        return render_template("signup.html")


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
