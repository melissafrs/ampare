from entity import Entity
from dbconnection import DBConnection

class Entrega(Entity):
    table_name = 'Entrega'

    def __init__(self, id, id_familia, endereco, data, hora):
        self.id = id
        self.id_familia = id_familia
        self.endereco = endereco
        self.data = data
        self.hora = hora

    def __str__ (self):
        return f"""Entrega: [{self.id}, {self.id_familia}, {self.endereco}, {self.data}, {self.hora}"""

    @staticmethod
    def loadFromId(id):
        query = f"""SELECT * FROM Entrega WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        if not row:
            raise Exception("Entrega com id "+ id + " não está cadastrada.")
        return Entrega(row.id, row.id_familia, row.endereco, row.data, row.hora)
    
    @staticmethod
    def loadAllEntities():
        query = f"""SELECT * FROM Entrega"""
        rows = DBConnection().executeQuery(query).fetchall()
        if not rows:
            raise Exception("Não conseguiu carregar entregas")
        
        return rows

    @staticmethod
    def loadAllEntitiesForFamily(id):
        query = f"""SELECT * FROM Entrega WHERE id_familia = {id}"""
        rows = DBConnection().executeQuery(query).fetchall()
        if not rows:
            raise Exception("Não conseguiu carregar entregas para familia {id}")
        
        return rows
