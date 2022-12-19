import Entity
import DBConnection

aliment = Alimento.loadFromId('1')
print(aliment)

class Alimento(Entity):
    table_name = 'Alimento'

    def __init__(self, id, cesta_id, tipo_alimento_id, data_validade):
        self.id = id
        self.cesta_id = cesta_id
        self.tipo_alimento_id = tipo_alimento_id
        self.data_validade = data_validade

    @staticmethod
    def loadFromId(self, id):
        query = """SELECT * FROM {table_name} WHERE id = {id}"""
        row = DBConnection().executeQuery(query).fetchone()
        return Alimento(row.id, row.cesta_id, row.tipo_alimento_id, row.data_validade)

