from alimento import Alimento
from cesta import Cesta
from tipoAlimento import TipoAlimento
from dbconnection import DBConnection

class FamiliaMutation:
    def __init__(self):
        self.connection = DBConnection()
    
    def register(self, nome, tamanho, ultima_entrega, proxima_entrega, endereco):
        query = self.queryInsert(nome, tamanho, ultima_entrega, proxima_entrega, endereco)
        self.execute(query)

    def delete(self, familia_id):
        query = self.queryDelete(familia_id)
        self.execute(query)
