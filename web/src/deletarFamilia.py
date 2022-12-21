from familiaMutation import FamiliaMutation
from cesta import Cesta
from entrega import Entrega
from entregaMutation import EntregaMutation
from cestaMutation import CestaMutation
from familia import Familia
from datetime import date

class DeletarFamilia:
    def __init__(self, id):
        self.id = id
    
    def execute(self):
        self.unsetPendingItems()
        mutation = FamiliaMutation()
        mutation.delete(self.id)

    def unsetPendingItems(self):
        pending_cestas = Cesta.loadNotENForFamilia(self.id)
        for cesta in pending_cestas:
            mutation_cesta = CestaMutation()
            mutation_cesta.setFamilia(cesta.id, None)
        pending_entregas = Entrega.loadAllEntitiesForFamily(self.id)
        for entrega in pending_entregas:
            if(date.fromisoformat(entrega.data) >= date.today()):
                mutation_entrega = EntregaMutation()
                mutation_entrega.setEndereco(entrega.id, None)


        
