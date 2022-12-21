import pyodbc

class DBConnection:

    def __init__(self):
        self.connection = pyodbc.connect(("Driver={SQL Server};""Server=LAPTOP-MEDAV53H;""Database=ampare"))

    def executeQuery(self, query):
        cursor = self.connection.cursor()
        return cursor.execute(query)
