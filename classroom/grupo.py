from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            if type(self._asignaturas)==list:
                self._asignaturas.append(Asignatura(x))
            else:
                self._asignaturas=[]
                self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if type(lista)==list:
            lista.append(alumno)
            if type(self.listadoAlumnos)==list:
                self.listadoAlumnos = self.listadoAlumnos + lista
            else:
                self.listadoAlumnos=[]
                self.listadoAlumnos+=lista
        else:
            lista=[]
            lista.append(alumno)
            if type(self.listadoAlumnos)==list:
                self.listadoAlumnos = self.listadoAlumnos + lista
            else:
                self.listadoAlumnos=[]
                self.listadoAlumnos+=lista

    def __str__(self):
        cadena="Grupo de estudiantes: "+self._grupo
        return cadena

    @ classmethod
    def asignarNombre(cls, nombre):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre
        
    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre

