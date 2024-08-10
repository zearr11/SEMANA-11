import mysql.connector

class ConexionBD:
    
    def __init__(self):
        self.conexion = mysql.connector.connect(host='localhost', database='bdnotas', user='root',password='123456')
        
    def getConexionBD(self):
        return self.conexion