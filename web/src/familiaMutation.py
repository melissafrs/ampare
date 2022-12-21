from alimento import Alimento
from cesta import Cesta
from dbconnection import DBConnection

class FamiliaMutation:
    def __init__(self):
        self.connection = DBConnection()
    
    def register(self, nome, tamanho, endereco):
        query = self.queryInsert(nome, tamanho, endereco)
        self.execute(query)

    def delete(self, familia_id):
        query = self.queryDelete(familia_id)
        self.execute(query)

    def update(self, familia_id, field, value):
        query = self.queryUpdate(familia_id, field, value)
        self.execute(query)


    def execute(self, query):
        rows_affected = self.connection.executeQuery(query)
        self.persist(query, rows_affected)
        rows_affected.commit()    

    def queryInsert(self, nome, tamanho, endereco):
        return f"""INSERT INTO Familia(nome, tamanho, endereco)
        VALUES('{nome}', {tamanho}, '{endereco}')
        """
    
    def queryDelete(self, familia_id):
        return f"""DELETE FROM Familia WHERE id = {familia_id}"""

    def queryUpdate(self, familia_id, field_name, data):
        return f"""UPDATE Familia SET {field_name} = '{data}' WHERE id = {familia_id}"""

    def persist(self, query, rows_affected):
        if rows_affected.rowcount != 1:
            raise Exception('Falha ao executar cadastro ', query)
