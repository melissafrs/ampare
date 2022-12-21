from entity import Entity
from dbconnection import DBConnection
import json

class Cesta(Entity):
    table_name = 'Cesta'

    def __init__(self, id, id_familia, status, entrega_id):
        self.id = id
        self.id_familia = id_familia
        self.status = status
        self.entrega_id = entrega_id

    @staticmethod
    def loadFromId(id):
        query = f"""SELECT * FROM Cesta WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        if not row:
            raise Exception("Cesta com id "+ id + " não está cadastrada.")
        return Cesta(row.id, row.id_familia, row.status, row.entrega_id)
    
    @staticmethod
    def loadFromEntregaId(id):
        query = f"""SELECT * FROM Cesta WHERE entrega_id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        if not row:
            raise Exception("Cesta com entrega id "+ id + " não está cadastrada.")
        return Cesta(row.id, row.id_familia, row.status, row.entrega_id)

    @staticmethod
    def loadNotENForFamilia(id):
        query = f"""SELECT * FROM Cesta WHERE id_familia ={id} AND status != 'EN' """
        return DBConnection().executeQuery(query).fetchall()       

    @staticmethod
    def loadAllEntities():
        query = f"""SELECT * FROM Cesta"""
        rows = DBConnection().executeQuery(query).fetchall()
        if not rows:
            raise Exception("Não conseguiu carregar Cestas")
        
        return rows

