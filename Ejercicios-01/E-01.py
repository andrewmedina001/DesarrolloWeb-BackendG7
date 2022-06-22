# Dibujar un rectangulo
print("\n\n___Funcion que dibuja un rectangulo__\n")
l=int(input("Ingrese la altura: "))
w=int(input("Ingrese el ancho: "))
print("")
for a in range(l):
    print("",end="")
    for an in range(w):
        print("#",end="")
    print("")