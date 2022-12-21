from familiaMutation import FamiliaMutation

class CadastrarFamilia:
    def __init__(self, nome, tamanho,  endereco):
        self.nome= str(nome)
        self.tamanho = int(tamanho)
        self.endereco= str(endereco)
    
    def execute(self):
        self.validateIsSpace()
        fm = FamiliaMutation()
        fm.register(self.nome, self.tamanho, self.endereco)

    def validateIsSpace(self):
        if self.nome.isspace() or self.tamanho < 0 or self.endereco.isspace() :
            raise Exception('Campos não preenchidos!')

