from alimento import Alimento
import pyodbc
from alimentoMutation import AlimentoMutation

tenta = AlimentoMutation().register('1', '12/12/2023')

todos = Alimento.loadAllEntities()

print(todos)

connect = pyodbc.connect(("Driver={SQL Server};""Server=DESKTOP-I3USHIT;""Database=ampare"))
cursor = connect.cursor()
cursor.execute("""select * from Alimento where id = 1""")
result = cursor.fetchone()
print ('o daqui: ', result)


alimento = Alimento.loadFromId('1')
print('o que veio: ',  alimento)
