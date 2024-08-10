import sys
from PyQt5 import QtWidgets, uic
from dao.CursoDao import CursoDao
from PyQt5.QtWidgets import QTableWidgetItem
from model.Curso import Curso

class CursoController:
    def __init__(self):
        
        self.app = QtWidgets.QApplication([])
        self.ventana = uic.loadUi("view/FRM_CURSOS.ui")
        
        self.ventana.tw_curlst.setColumnWidth(0,65)
        self.ventana.tw_curlst.setColumnWidth(1,250)
        self.ventana.tw_curlst.setColumnWidth(2,60)
        
        self.ventana.tw_curlst.cellClicked.connect(self.onCellClickTblCursos)
        self.ventana.pb_save.clicked.connect(self.onClick_BtSave)
        self.ventana.pb_new.clicked.connect(self.onClick_btNuevo)
        
        
        self.CursoDao = CursoDao()
        self.listar_curso()
        
        self.ventana.show()
        self.app.exec()
        
    def onClick_BtSave(self):
        idCurso = self.ventana.le_cod.text()
        Nombre = self.ventana.le_name.text()
        Credito = self.ventana.le_credit.text()
        NuevoCurso = Curso(idCurso, Nombre, Credito)
        if self.ventana.le_cod.isEnabled():
            self.CursoDao.insertarCursos(NuevoCurso)
        else:
            self.CursoDao.actualizarCurso(NuevoCurso)
        self.listar_curso()
        
    def onClick_btNuevo(self):
        self.ventana.le_cod.setText("")
        self.ventana.le_cod.setEnabled(True)
        self.ventana.le_name.setText("")
        self.ventana.le_credit.setText("")
        
    def onCellClickTblCursos(self, fila):
        idcurso = self.ventana.tw_curlst.item(fila, 0).text()
        self.ventana.le_cod.setText(idcurso)
        self.ventana.le_cod.setEnabled(False)
        objCurso = self.CursoDao.ObtenerCurso(idcurso)
        self.ventana.le_name.setText(objCurso[1])
        self.ventana.le_credit.setText(str(objCurso[2]))
                
    def listar_curso(self):
        listaCursos = self.CursoDao.listarCursos()
        cantidad = len(listaCursos)
        self.ventana.tw_curlst.setRowCount(cantidad)
        fila = 0
        for objCurso in listaCursos:
            self.ventana.tw_curlst.setItem(fila, 0, QTableWidgetItem(objCurso[0]))
            self.ventana.tw_curlst.setItem(fila, 1, QTableWidgetItem(objCurso[1]))
            self.ventana.tw_curlst.setItem(fila, 2, QTableWidgetItem(str(objCurso[2])))
            fila +=1
            
            