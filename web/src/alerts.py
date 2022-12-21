from entrega import Entrega
from datetime import date, time

class Alerts:

    def __init__(self, data, type):
        self.data = data
        self.type = type
    
    @staticmethod
    def loadEntregas(date):
        ealerts = Entrega.loadAllEntitiesSinceDate(date)
        alers = []
        for ealert in ealerts:
            data = Alerts.getDateFormatted(ealert.data)
            alert = Alerts(data, 'entrega')
            alert.time = Alerts.getTimeFormatted(ealert.hora)
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
