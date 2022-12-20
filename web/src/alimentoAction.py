from alimento import Alimento
from flask import Flask, redirect, url_for, render_template

class AlimentoAction:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("web/src/pages/Food/index.html")

    @app.route("/addFood", methods=["POST", "GET"])
    def addFood():
        return render_template("web/src/pages/Food/addFood.html")

    @app.route("/<usr>")
    def user(usr):
        return f"<h1>{usr}</h1>"

    def listAll():
        return Alimento.loadAllEntities()

    def register():
        pass

