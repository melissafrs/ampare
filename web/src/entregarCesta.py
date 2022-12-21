from cestaMutation import CestaMutation
from cesta import Cesta
from datetime import datetime

class EntregarCesta:
    def __init__(self, id):
        self.id = id
    
    def execute(self):
        self.validateCestaConfirmed()
        mutation = CestaMutation()
        mutation.setStatus(self.id, 'EN')

    def validateCestaConfirmed(self):
        if Cesta.loadFromId(self.id).status != 'CO':
            raise Exception('Cesta não confirmada, não pode ser entregue!')
