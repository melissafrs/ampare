from familiaMutation import FamiliaMutation

class CadastrarFamilia:
    def __init__(self, nome, tamanho,  endereco):
        self.fields = nome
        self.tamanho = tamanho
        self.endereco = endereco
    
    def execute(self):
        self.validateIsSpace()
        self.toType()
        fm = FamiliaMutation()
        fm.register(self.nome, self.tamanho, self.endereco)

    def validateIsSpace(self):
        if self.nome.isspace() or int(self.tamanho) < 0 or self.endereco.isspace() :
            raise Exception('Campos não preenchidos!')
            
    def toType(self):
        self.nome= str(self.nome)
        self.tamanho = int(self.tamanho)
        self.endereco= str(self.endereco)
