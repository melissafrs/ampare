from flask import Flask, redirect, url_for, render_template, request
from alimento import Alimento 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Dashboard/index.html")

@app.route("/food")
def food():
    return render_template("Food/index.html")

@app.route("/family")
def family():
    return render_template("Family/index.html")

if __name__ == "__main__":
    app.run(debug=True)