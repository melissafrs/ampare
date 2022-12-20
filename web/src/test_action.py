from flask import Flask, redirect, url_for, render_template, request
from alimento import Alimento
from familia import Familia

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Dashboard/index.html")

@app.route("/food")
def food():
    return render_template("Food/index.html")

@app.route("/family")
def family():
    familias = Familia.loadAllEntities()
    return render_template("Family/index.html", familias=familias)

@app.route("/family-details-<id>")
def familyDetails(id):
    familia = Familia.loadFromId(id)
    return render_template("Family/details.html", familia=familia)

if __name__ == "__main__":
    app.run(debug=True)