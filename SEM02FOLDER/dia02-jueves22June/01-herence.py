#
# Polimorfismo en Python
#   definicion del mismo metodo en diferentes clases pero con un 
#   comportamiento diferente. 
class User:
    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    def info(self):
        return{
            'nombre':self.nombre,
            'apellido':self.apellido,
        }

class Alumno(User):
    # Constructor
    def __init__(self,Nombre,apellido2,anio,section):
        self.anio=anio
        self.section=section
        # metodo que sirve para utilizar los metodos y atriutos de la clase padre

        super().__init__(nombre=Nombre,apellido=apellido2)
    def info(self):
        infoUser=super().info()
        data={
            'anio':self.anio,
            'seccion':self.section
        }
        return {**data,**infoUser}

alumnoEduardo=Alumno('Eduardo','De Rivero','Sexto','A')
usuarioReal=User('Raul','Mendoza')

informacion=alumnoEduardo.info()
print(informacion)