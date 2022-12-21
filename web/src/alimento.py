from entity import Entity
from dbconnection import DBConnection

class Alimento(Entity):
    table_name = 'Alimento'

    def __init__(self, id, cesta_id, tipo_alimento_id, data_validade):
        self.id = id
        self.cesta_id = cesta_id
        self.tipo_alimento_id = tipo_alimento_id
        self.data_validade = data_validade

    def __str__ (self):
        return f"""Alimento: [{self.id}, {self.cesta_id}, {self.tipo_alimento_id}, {self.data_validade}"""

    @staticmethod
    def loadFromId(id):
        query = f"""SELECT * FROM Alimento WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        if not row:
            raise Exception("Alimento com id "+ id + " não está cadastrado.")
        return Alimento(row.id, row.cesta_id, row.tipo_alimento_id, row.data_validade)
    
    @staticmethod
    def loadAllEntities():
        query = f"""SELECT * FROM Alimento"""
        rows = DBConnection().executeQuery(query).fetchall()
        if not rows:
            raise Exception("Não conseguiu carregar Alimentos")
        
        return rows
    
    @staticmethod
    def loadAllEntitiesForCesta(id):
        query = f"""SELECT * FROM Alimento WHERE cesta_id ={id}"""
        rows = DBConnection().executeQuery(query).fetchall()
        if not rows:
            raise Exception("Não conseguiu carregar Alimentos")
        
        return rows
