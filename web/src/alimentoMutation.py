from alimento import Alimento
from cesta import Cesta
from tipoAlimento import TipoAlimento
from dbconnection import DBConnection

class AlimentoMutation:
    def __init__(self):
        self.connection = DBConnection()
    
    def register(self, type_id, expiration_date):
        type = TipoAlimento.loadFromId(type_id)
        query = self.queryInsert(type.id, expiration_date)
        self.execute(query)

    def delete(self, alimento_id):
        query = self.queryDelete(alimento_id)
        self.execute(query)

    def setCesta(self, alimento_id, cesta_id):
        cesta = Cesta.loadFromId(cesta_id)
        query = self.queryUpdate(alimento_id, 'cesta_id', cesta.id)
        self.execute(query)

    def setExpirationDate(self, alimento_id, expiration_date):
        query = self.queryUpdate(alimento_id,'data_validade', expiration_date)
        self.execute(query)

    def execute(self, query):
        rows_affected = self.connection.executeQuery(query)
        self.persist(query, rows_affected)
        rows_affected.commit()

    def queryInsert(self, type_id, expiration_date):
        return f"""INSERT INTO Alimento(cesta_id, tipo_alimento_id, data_validade)
        VALUES(NULL,  {type_id}, '{expiration_date}')
        """
    
    def queryDelete(self, alimento_id):
        return f"""DELETE FROM Alimento WHERE id = {alimento_id}"""

    def queryUpdate(self, alimento_id, field_name, data):
        return f"""UPDATE Alimento SET {field_name} = '{data}' WHERE id = {alimento_id}"""

    def persist(self, query, rows_affected):
        if rows_affected.rowcount != 1:
            raise Exception('Falha ao executar cadastro ', query)


