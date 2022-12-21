from cesta import Cesta
from familia import Familia
from alimento import Alimento
from tipoAlimento import TipoAlimento
from entrega import Entrega
from datetime import date, time

class CestaAction:

    def __init__(self, id, data = 0, family = 0, peso = 0):
        self.id = id
        self.data = data
        self.family = family
        self.peso = peso
    
    @staticmethod
    def loadData():
        cestas = Cesta.loadAllEntities()
        cdata = []
        for cesta in cestas:
            try:
                family = Familia.loadFromId(cesta.id_familia)
                peso = CestaAction.calculatePeso(Alimento.loadAllEntitiesForCesta(cesta.id))
                entrega = Entrega.loadFromCestaId(cesta.id)
                data = CestaAction.getDateFormatted(entrega.data)
                action = CestaAction(cesta.id, data, family.nome, peso)
            except (Exception) as e:
                action = CestaAction(cesta.id, data, family.nome, peso)

            cdata.append(action)
        
        return cdata

    @staticmethod
    def calculatePeso(alimentos):
        peso = 0.0
        for alimento in alimentos:
            tipo = TipoAlimento.loadFromId(alimento.tipo_alimento_id)
            peso = tipo.peso + peso

    @staticmethod
    def getDateFormatted(input):
        input = date.fromisoformat(input)
        return f"{input.day}/{input.month}"
