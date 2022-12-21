from entity import Entity
import json
from dbconnection import DBConnection

class TipoAlimento(Entity):
    table_name = 'TipoAlimento'

    def __init__(self, id, nome, peso, descricao):
        self.id = id
        self.nome = nome
        self.peso = peso
        self.descricao = descricao

    def __str__ (self):
        return f"""Alimento: [{self.id}, {self.nome}, {self.peso}, {self.descricao}"""

    @staticmethod
    def loadFromId(id):
        query = f"""SELECT * FROM TipoAlimento WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        if not row:
            raise Exception("Alimento com id "+ id + " não está cadastrado.")
        return TipoAlimento(row.id, row.nome, row.peso, row.descricao)
    
    @staticmethod
    def loadAllEntities():
        query = f"""SELECT * FROM TipoAlimento"""
        rows = DBConnection().executeQuery(query).fetchall()
        if not rows:
            raise Exception("Não conseguiu carregar TipoAlimentos")
        
        return rows
