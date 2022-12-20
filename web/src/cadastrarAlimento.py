from alimentoMutation import AlimentoMutation
from datetime import datetime

class CadastrarAlimento:
    def __init__(self, type_id, expiration_date):
        self.type_id = type_id
        self.expiration_date = expiration_date
    
    def execute(self):
        self.validateExpirationDate()
        AlimentoMutation.register(self.type_id, self.expiration_date)

    def validateExpirationDate(self):
        if datetime.strptime(self.expiration_date, '%d/%m/%Y') <= datetime.now():
            raise Exception('Alimento vencido!')
