from flask import Flask, redirect, url_for, render_template, request
from alimento import Alimento
from cesta import Cesta
from cestaAction import CestaAction
from familia import Familia
from entrega import Entrega
from alerts import Alerts
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    alerts_entregas = Alerts.loadEntregas(date.today())
    return render_template("Dashboard/index.html", alerts_entregas = alerts_entregas)

@app.route("/food")
def food():
    cestas = CestaAction.loadData()
    return render_template("Food/index.html", cestas = cestas)

@app.route("/family", methods=['GET', 'POST'])
def family():
    familias = Familia.loadAllEntities()
    return render_template("Family/index.html", familias = familias)

@app.route("/family-details-<id>")
def familyDetails(id):
    familia = Familia.loadFromId(id)
    entregas = Entrega.loadAllEntitiesForFamily(id)
    return render_template("Family/details.html", familia = familia, entregas = entregas)

@app.route("/add-family", methods=['GET', 'POST'])
def addFamily():
    if request.method == 'POST':
        name = request.form['fname']
        nmembers = request.form['nmembers']
        sname = request.form['sname']
        return render_template("Family/addFamily.html")
    
@app.route("/add-food")
def addFood():
    return render_template("Food/addFood.html")

if __name__ == "__main__":
    app.run(debug=True)