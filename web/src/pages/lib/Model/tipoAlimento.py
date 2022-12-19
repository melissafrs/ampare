from entity import Entity
from dbconnection import DBConnection

class TipoAlimento(Entity):
    table_name = 'TipoAlimento'

    def __init__(self, id, nome, peso, descricao):
        self.id = id
        self.nome = nome
        self.peso = peso
        self.descricao = descricao

    @staticmethod
    def loadFromId(id):
        query = f"""SELECT * FROM TipoAlimento WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        if not row:
            raise Exception("TipoAlimento com id "+ id + " não está cadastrado.")
        return TipoAlimento(row.id, row.nome, row.peso, row.descricao)

