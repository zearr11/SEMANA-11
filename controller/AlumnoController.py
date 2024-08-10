from PyQt5 import QtWidgets, uic
from dao.AlumnoDao import AlumnoDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Alumno import Alumno

class AlumnoControleer:
    
    def __init__(self):
        
        self.app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/FRM_ALUMNOS.ui")
        self.ventana.show()
        self.app.exec()