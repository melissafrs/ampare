from alimento import Alimento
import pyodbc
from entrega import Entrega
from alerts import Alerts
from datetime import date

todos = Alerts.loadEntregas(date.today())

print(todos)

connect = pyodbc.connect(("Driver={SQL Server};""Server=DESKTOP-I3USHIT;""Database=ampare"))
cursor = connect.cursor()
cursor.execute("""select * from Alimento where id = 1""")
result = cursor.fetchone()
print ('o daqui: ', result)


alimento = Alimento.loadFromId('1')
print('o que veio: ',  alimento)
