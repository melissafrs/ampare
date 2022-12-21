from familia import Familia
from dbconnection import DBConnection

class EntregaMutation:
    def __init__(self):
        self.connection = DBConnection()
    
    def register(self, id_familia, data, hora, cesta_id, endereco):
        query = self.queryInsert(id_familia, data, hora, cesta_id, endereco)
        self.execute(query)

    def delete(self, id):
        query = self.queryDelete(id)
        self.execute(query)

    def setFamilia(self, id, familia_id):
        familia = Familia.loadFromId(familia_id)
        query = self.queryUpdate(id, 'id_familia', familia_id)
        self.execute(query)
    
    def setEndereco(self, id, endereco):
        query = self.queryUpdate(id, 'endereco', endereco)
        self.execute(query)
    
    
    def setData(self, id, new_data):
        query = self.queryUpdate(id, 'data', new_data)
        self.execute(query)


    def execute(self, query):
        rows_affected = self.connection.executeQuery(query)
        self.persist(query, rows_affected)
        rows_affected.commit()

    def queryInsert(id_familia, data, hora, cesta_id, endereco):
        return f"""INSERT INTO Entrega(id_familia, endereco, data, hora, cesta_id)
        VALUES({id_familia}, {endereco}, {data}, {hora}, {cesta_id})
        """
    
    def queryDelete(self, id):
        return f"""DELETE FROM Entrega WHERE id = {id}"""

    def queryUpdate(self, id, field_name, data):
        return f"""UPDATE Entrega SET {field_name} = '{data}' WHERE id = {id}"""

    def persist(self, query, rows_affected):
        if rows_affected.rowcount != 1:
            raise Exception('Falha ao executar ', query)