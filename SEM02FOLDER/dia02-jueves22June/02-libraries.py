from camelcase import CamelCase

c=CamelCase()

parrafo="hola amigos coños"
result=c.hump(parrafo)
print(result)
print("hola amigos coños")