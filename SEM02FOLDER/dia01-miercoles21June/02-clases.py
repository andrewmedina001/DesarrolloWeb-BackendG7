# POO
class Persona:
    est=100
    colorOjos='Cafe'
    colorCabello='Negro'
    fechaNacimiento='2000-01-01'

    def saludar(self):
        print('Hola buenos dias')

personaEduardo=Persona()
print(personaEduardo.fechaNacimiento)

personaMaria=Persona()
personaMaria.colorOjos='Rojo'
print(personaMaria.colorOjos)
print(personaMaria.colorCabello)

personaEduardo.saludar()
personaMaria.saludar()


# Constructor

    # 

class Mascota:
    def __init__(self,nombre,especie,raza,sexo):
        self.nombre=nombre
        self.especie=especie
        self.raza=raza
        self.sexo=sexo

    def info(self):
        print(self.nombre)
        print(self.especie)
        print(self.raza)
        print(self.sexo)

mascota01=Mascota('Alrea','perro','chitsu','F')
mascota01.info()