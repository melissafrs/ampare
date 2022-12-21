from entrega import Entrega
from datetime import date, time

class Alerts:

    def __init__(self, data, tipo):
        self.data = data
        self.tipo = tipo
    
    @staticmethod
    def loadEntregas():
        ealerts = Entrega.loadAllEntitiesSinceDate(date.today())
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
        if (input == date.today):
            return 'hoje'
        
        return input.day + '/' + input.month
    
    @staticmethod
    def getTimeFormatted(input):
        input = time.fromisoformat(input)
        return input.hour + 'h' + input.minute
