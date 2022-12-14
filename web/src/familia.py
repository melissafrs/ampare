from entity import Entity
import json
from dbconnection import DBConnection

class Familia(Entity):
    table_name = 'Familia'

    def __init__(self, id, nome, tamanho, proxima_entrega, endereco):
        self.id = id
        self.nome = nome
        self.tamanho = tamanho
        self.endereco = endereco
        self.proxima_entrega = proxima_entrega

    def __str__ (self):
        return f"""Familia: [{self.id}, {self.nome}, {self.tamanho}, {self.endereco}, {self.proxima_entrega}"""

    @staticmethod
    def loadFromId(id):
        query = f"""SELECT * FROM Familia WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        if not row:
            raise Exception("Familia com id "+ id + " não está cadastrado.")
        return Familia(row.id, row.nome, row.tamanho, row.proxima_entrega, row.endereco)
    
    @staticmethod
    def loadAllEntities():
        query = f"""SELECT * FROM Familia"""
        rows = DBConnection().executeQuery(query).fetchall()
        if not rows:
            raise Exception("Não conseguiu carregar Familia")
            
        return rows
