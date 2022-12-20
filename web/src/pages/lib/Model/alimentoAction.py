from alimento import Alimento
from flask import Flask, redirect, url_for, render_template

class AlimentoAction:
    app = Flask(__name__)

    @app.route("/")
    def home():
        return render_template("web\src\pages\Food\index.html")
        
    def listAll():
        return Alimento.loadAllEntities()

    def register():
        pass

