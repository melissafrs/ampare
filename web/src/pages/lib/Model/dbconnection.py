import pyodbc

class DBConnection:
    server = 'DESKTOP-I3USHIT' #teu hostname aqui

    def __init__(self):
        self.connection = pyodbc.connect(("Driver={SQL Server};""Server=DESKTOP-I3USHIT;""Database=ampare"))

    def executeQuery(self, query):
        cursor = self.connection.cursor()
        return cursor.execute(query)
