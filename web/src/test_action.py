from flask import Flask, redirect, url_for, render_template, request
from alimento import Alimento
from cesta import Cesta
from cestaAction import CestaAction
from familia import Familia
from entrega import Entrega
from entregasAction import EntregasAction
from datetime import date
from cadastrarFamilia import CadastrarFamilia
from entregarCesta import EntregarCesta
from deletarFamilia import DeletarFamilia

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def home():
    alerts_entregas = EntregasAction.loadEntregas(date.today())
    return render_template("Dashboard/index.html", alerts_entregas = alerts_entregas)

@app.route("/delivery/<id>")
def deliveryDetails(id):
    delivery = cesta = action = []
    try:
        delivery = Entrega.loadFromId(id)
        cesta = Cesta.loadFromEntregaId(id)
        action = CestaAction.loadDataForId(cesta.id)
    except:
        pass
    return render_template("Delivery/index.html", entrega = delivery, cesta = action, status = cesta)

@app.route("/deliveryCesta-<id>")
def deliveryCesta(id):
    command = EntregarCesta(id)
    command.execute()
    return deliveryDetails(id)

@app.route("/food")
def food():
    cestas = CestaAction.loadData()
    return render_template("Food/index.html", cestas = cestas)

@app.route("/food/<id>")
def foodDetails(id):
    cesta = details = []
    try:
        cesta = CestaAction.loadDataForId(id)
        details = CestaAction.loadDetailsForCesta(id)
    except:
        pass
    return render_template("Food/details.html", cesta = cesta, details = details)

@app.route("/family", methods=['GET', 'POST'])
def family():
    familias = Familia.loadAllEntities()
    return render_template("Family/index.html", familias = familias)

@app.route("/family/<id>")
def familyDetails(id):
    familia = entregas = []
    try:
        familia = Familia.loadFromId(id)
        entregas = Entrega.loadAllEntitiesForFamily(id)
    except:
        pass
    return render_template("Family/details.html", familia = familia, entregas = entregas)

@app.route("/add-family", methods=['GET', 'POST'])
def addFamily():
    if request.method == 'POST':
        name = request.form['fname']
        members = request.form['nmembers']
        name = request.form['sname']
        cf = CadastrarFamilia(name, members, name)
        cf.execute()
        return render_template("Family/index.html")
    if request.method == 'GET':
        return render_template("Family/addFamily.html")

@app.route("/update-family/<id>", methods=['GET', 'POST'])
def updateFamily(id):
    familia = Familia.loadFromId(id)
    if request.method == 'POST':
        familia.nome = request.form['fname']
        familia.tamanho = request.form['nmembers']
        familia.endereco = request.form['sname']
        

        return render_template("Family/index.html")
    if request.method == 'GET':
        return render_template("Family/updateFamily.html", familia = familia)

@app.route("/delete-family/<id>")
def deleteFamily(id):
    command = DeletarFamilia(id)
    command.execute()
    return home()


@app.route("/add-food")
def addFood():
    return render_template("Food/addFood.html")

if __name__ == "__main__":
    app.run(debug=True)