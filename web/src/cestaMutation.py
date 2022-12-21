from familia import Familia
from dbconnection import DBConnection

class CestaMutation:
    def __init__(self):
        self.connection = DBConnection()
    
    def register(self, id_familia, status, entrega_id):
        query = self.queryInsert(id_familia, status, entrega_id)
        self.execute(query)

    def delete(self, cesta_id):
        query = self.queryDelete(cesta_id)
        self.execute(query)

    def setFamilia(self, cesta_id, familia_id):
        familia = Familia.loadFromId(familia_id)
        query = self.queryUpdate(cesta_id, 'familia_id', familia_id)
        self.execute(query)
    
    
    def setStatus(self, cesta_id, new_status):
        query = self.queryUpdate(cesta_id, 'status', new_status)
        self.execute(query)


    def execute(self, query):
        rows_affected = self.connection.executeQuery(query)
        self.persist(query, rows_affected)
        rows_affected.commit()

    def queryInsert(self, id_familia, status, entrega_id):
        return f"""INSERT INTO Cesta(id_familia, status, entrega_id)
        VALUES(NULL,  {id_familia}, {status}, {entrega_id})
        """
    
    def queryDelete(self, cesta_id):
        return f"""DELETE FROM Cesta WHERE id = {cesta_id}"""

    def queryUpdate(self, cesta_id, field_name, data):
        return f"""UPDATE Cesta SET {field_name} = '{data}' WHERE id = {cesta_id}"""

    def persist(self, query, rows_affected):
        if rows_affected.rowcount != 1:
            raise Exception('Falha ao executar cadastro ', query)