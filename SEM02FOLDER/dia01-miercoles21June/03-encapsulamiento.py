# Pilares
    # 1. Abstraccion
    # 2. Encapsulamiento
    # 3. Herencia
    # 4. Polimorfismo

# Evitar posibles metodos o atriubtos 

class Vehiculo:
    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        # si queremos indicar que un atributo de la clase va a ser privado
            # (no va a poder ser accedido desde fuera de la clase)
            # tendremos que colocar al inicio el nombre del atributo
        self.__serie=marca+modelo
        # Protegidos en python tienen un comportamiento diferente y mas que todo sirve 
            # Para que al momento de hacer herencia no se modifique los valores al crear 
            # el mismo atributo al crear el mismo atributo en clases hijas
        self._serie2=marca+modelo

        def mostrarSerie():
            print("serie is")