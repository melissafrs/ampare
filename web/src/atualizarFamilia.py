from familia import Familia
from familiaMutation import FamiliaMutation

class AtualizarFamilia():

    def __init__(self, id, nome = None, tamanho= None, endereco = None):
        self.id = id
        self.nome = nome
        self.tamanho = tamanho
        self.endereco = endereco

    def execute(self):
        mutation = FamiliaMutation()
        if(self.nome):
            mutation.update(self.id, 'nome', self.nome)
        if(self.tamanho):
            mutation.update(self.id, 'tamanho', self.tamanho)
        if(self.endereco):
            mutation.update(self.id, 'endereco', self.endereco)

    
