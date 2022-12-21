from entrega import Entrega
from datetime import date, time

class EntregasAction:

    def __init__(self, id, data, type):
        self.id = id
        self.data = data
        self.type = type
    
    @staticmethod
    def loadEntregas(date):
        ealerts = Entrega.loadAllEntitiesSinceDate(date)
        alers = []
        for ealert in ealerts:
            data = EntregasAction.getDateFormatted(ealert.data)
            alert = EntregasAction(ealert.id, data, 'entrega')
            alert.time = EntregasAction.getTimeFormatted(ealert.hora)
            alert.details = ealert.endereco
            alert.extra_id = ealert.cesta_id
            alers.append(alert)
        
        return alers

    @staticmethod
    def getDateFormatted(input):
        input = date.fromisoformat(input)
        if (input == date.today()):
            return 'hoje'
        
        return f"{input.day}/{input.month}"
    
    @staticmethod
    def getTimeFormatted(input):
        input = time.fromisoformat(input)
        return f"{input.hour}h{input.minute}"
