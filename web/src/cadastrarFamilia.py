from familiaMutation import FamiliaMutation

class CadastrarFamilia:
    def __init__(self, nome, tamanho,  endereco):
        self.nome = nome
        self.tamanho = tamanho
        self.endereco = endereco
    
    def execute(self):
        self.validateIsSpace()
        FamiliaMutation.register(self.type_id, self.expiration_date)

    def validateIsSpace(self):
        if self.nome.isspace() or self.tamanho.isspace() or self.endereco.isspace() :
            raise Exception('Campos não preenchidos!')
