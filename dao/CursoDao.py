from util.ConexionBD import ConexionBD

class CursoDao:
    
    def __init__(self):
        self.conexion = ConexionBD().getConexionBD()
        
    def listarCursos(self):
        cursor = self.conexion.cursor()
        sql = 'SELECT idcurso, nomcurso, credito FROM curso ORDER BY idcurso desc'
        cursor.execute(sql)
        return cursor.fetchall()
    
    def ObtenerCurso(self, idcCurso):
        cursor = self.conexion.cursor()
        sql = "SELECT idcurso, nomcurso, credito FROM CURSO WHERE idcurso = '{}'".format(idcCurso)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def actualizarCurso(self, curso):
        exec = self.conexion.cursor()
        query = "UPDATE CURSO SET nomcurso = '{}', credito = '{}' where idcurso = '{}'".format(curso.name_curso, curso.credito, curso.idcurso)
        exec.execute(query)
        self.conexion.commit()
        exec.close()
        
    
    def insertarCursos(self, curso):
        exec = self.conexion.cursor()
        query = "INSERT INTO curso values ('{}','{}','{}')".format(curso.idcurso, curso.name_curso, curso.credito)
        exec.execute(query)
        self.conexion.commit()
        exec.close()
        