# 
def saludarN(name):
    """textttt into gucci"""
    print("Hola {} como estais?".format(name))
saludarN("Andrew")
e=[]
def regElec(nombre,precio,almacen='Las malvinas'):
    e.append({'nombre':nombre,'precio':precio,'almacen':almacen})
    return True
regElec('Licuadora 12v',115.00)
regElec('Freidora de Aire',100.00,'Cercado')
regElec('Secador de cabello',140)
print(len(e))

a=[1,2,3]
del a[0]
print(a)
b=(1,4,5)
print(b)
z={10,5,7}
print(z)

# Recepcion de numero indeterminado de valores
def funcionSinFinValores(clase,*valores):
    # Lo convierte en una tupla
    print(type(valores))
    listamia=list(valores)
    print(type(listamia))
    print(listamia)

funcionSinFinValores('abx','abc','acd')
funcionSinFinValores('abx','abc','acd','gucci')