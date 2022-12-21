from alimento import Alimento
from cesta import Cesta
from tipoAlimento import TipoAlimento
from dbconnection import DBConnection

class FamiliaMutation:
    def __init__(self):
        self.connection = DBConnection()
    
    def register(self, nome, tamanho, proxima_entrega, endereco):
        query = self.queryInsert(nome, tamanho, proxima_entrega, endereco)
        self.execute(query)

    def delete(self, familia_id):
        query = self.queryDelete(familia_id)
        self.execute(query)

    

    def queryInsert(self, nome, tamanho, endereco):
        return f"""INSERT INTO Familia(id, nome, tamanho, endereco)
        VALUES(NULL,  {nome}, {tamanho}, {endereco})
        """
    
    def queryDelete(self, familia_id):
        return f"""DELETE FROM Familia WHERE id = {familia_id}"""

    def queryUpdate(self, familia_id, field_name, data):
        return f"""UPDATE Familia SET {field_name} = '{data}' WHERE id = {familia_id}"""

    def persist(self, query, rows_affected):
        if rows_affected.rowcount != 1:
            raise Exception('Falha ao executar cadastro ', query)
