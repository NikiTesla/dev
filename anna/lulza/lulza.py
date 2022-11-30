from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///lulza.db'
db = SQLAlchemy(app)

class Fact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f'Fact {self.id}'

@app.route("/")
def index():
    return render_template("main.html")


@app.route("/facts")
def facts():
    facts = Fact.query.order_by(Fact.date).all()
    return render_template("facts.html", facts=facts)


@app.route("/add_fact", methods=['POST', 'GET'])
def add_fact():
    if request.method == "POST":
        fact_name = request.form['name']
        fact_text = request.form['text']

        fact = Fact(name=fact_name, text=fact_text)
        
        try:
            db.session.add(fact)
            db.session.commit()
            return redirect('/facts')
        except:
            return "Error occured"
    else:
        return render_template("add_fact.html")


@app.route("/fact/<int:id>")
def fact(id):
    print(f"selected {id} fact")
    fact = Fact.query.get(id)
    return render_template("fact.html", fact=fact)


@app.route("/photos")
def photos():
    return render_template("photos.html")


if __name__== "__main__":
    app.run(debug=True, host="0.0.0.0")