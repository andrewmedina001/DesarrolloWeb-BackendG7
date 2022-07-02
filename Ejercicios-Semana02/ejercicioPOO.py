
# crear una clase Persona en la cual se guarden su nombre, 
    # fecha_nacimiento, nacionalidad, dni, ademas tambien una 
    # clase Alumno y una clase Docente en la cual el alumno , 
    # a diferencia del docente, tenga una serie de cursos matriculados, 
    # y el docente por su parte tenga un numero del seguro social y 
    # su cuenta de la CTS. En base a lo visto de herencia crear las clases 
    # y ademas ver si hay algun atributo o metodo que deba de ser privado

from operator import truediv


class Persona:
    def __init__(self,nombre,fecha_nacimiento,nacionalidad,dni,):
        self.nombre=nombre
        self.fecha_nacimiento=fecha_nacimiento
        self.dni=dni
        self.nacionalidad=nacionalidad
    def info(self):
        return{
            'nombre':self.nombre,
            'fecha_nacimiento':self.fecha_nacimiento,
            'dni':self.dni,
            'nacionalidad':self.nacionalidad
        }
    

class Alumno(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni,curso01=False,curso02=False,curso03=False,curso04=False,curso05=False):
        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)
        self.curso01=curso01
        self.curso02=curso02
        self.curso03=curso03
        self.curso04=curso04
        self.curso05=curso05
    
    def info(self):
        InfoUser=super().info()
        data={
            'curso01':self.curso01,
            'curso02':self.curso02,
            'curso01':self.curso03,
            'curso01':self.curso04,
            'curso01':self.curso05
        }
        return {**InfoUser,**data}

class Docente(Persona):
    def __init__(self, nombre, fecha_nacimiento, nacionalidad, dni,num_seguro_social,cuentaCTS):
        super().__init__(nombre, fecha_nacimiento, nacionalidad, dni)

        # Atributos Protegidos
        self._num_seguro_social=num_seguro_social
        self._cuentaCTS=cuentaCTS
    def info(self):
        InfoUser=super().info()
        data={
            'numSeguroSocial':self._num_seguro_social,
            'cuentaCTS':self._cuentaCTS
        }
        return {**InfoUser,**data}


alumnoAndrew=Alumno('Andrew','1001-01-01','Peru','87654321','True','True','True','True','True')
docente01=Docente('nombreDocente','1010-10-10','Colombia','12346578','999999999','10101010')

print(alumnoAndrew.info())
print(docente01.info())