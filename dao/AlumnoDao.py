from util.ConexionBD import ConexionBD

class AlumnoDao:
    def __init__(self):
        self.conexion = ConexionBD().getConexionBD()
        
    def listarAlumnos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT a.IdAlumno, a.NomAlumno, a.ApeAlumno, e.NomEsp from alumno a inner join especialidad e ON a.IdEsp = e.IdEsp order by a.IdAlumno desc"
        cursor.execute(sql)
        return cursor.fetchall()
    
    def ObtenerAlumno(self, idAlumno):
        cursor = self.conexion.cursor()
        sql = "SELECT a.IdAlumno, a.NomAlumno, a.ApeAlumno, e.NomEsp from alumno a inner join especialidad e ON a.IdEsp = e.IdEsp WHERE a.IdAlumno = '{}'".format(idAlumno)
        cursor.execute(sql)
        return cursor.fetchone()
    
    def insertarAlumno(self, alumno):
        exec = self.conexion.cursor()
        query = "INSERT INTO alumno(IdAlumno, NomAlumno, ApeAlumno, IdEsp, Proce) values ('{}','{}','{}','{}')".format(alumno.cod_alumno, alumno.name_alumno, alumno.last_alumno, alumno.idespecialidad, alumno.procedencia)
        exec.execute(query)
        self.conexion.commit()
        exec.close()
    
    def actualizarAlumno(self, alumno):
        exec = self.conexion.cursor()
        query = "UPDATE alumno SET IdAlumno = '{}', NomAlumno = '{}', ApeAlumno = '{}', IdEsp = '{}', Proce = '{}' where IdAlumno = '{}'".format(alumno.cod_alumno, alumno.name_alumno, alumno.last_alumno, alumno.idespecialidad, alumno.procedencia)
        exec.execute(query)
        self.conexion.commit()
        exec.close()
