from util.ConexionBD import ConexionBD

class CursoDao:
    
    def __init__(self):
        self.conexion = ConexionBD().getConexionBD()
        
    def listarCursos(self):
        cursor = self.conexion.cursor()
        sql = 'SELECT * FROM CURSO ORDER BY idcurso DESC'
        cursor.execute(sql)
        return cursor.fetchall()
    
    def insertarCursos(self, curso):
        exec = self.conexion.cursor()
        query = "INSERT INTO curso values ('{}','{}','{}')".format(curso.idcurso, curso.name_cursom, curso.credito)
        exec.execute(query)
        self.conexion.commit()
        exec.close()
        