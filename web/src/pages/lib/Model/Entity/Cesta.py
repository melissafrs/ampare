import Entity
import DBConnection

class Cesta(Entity):
    table_name = 'Cesta'

    def __init__(self, id, id_familia, status, entrega_id):
        self.id = id
        self.id_familia = id_familia
        self.status = status
        self.entrega_id = entrega_id

    @staticmethod
    def loadFromId(self, id):
        query = """SELECT * FROM {table_name} WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        return Cesta(row.id, row.id_familia, row.status, row.data_validade, row.entrega_id)

