# dibujar un octogono
print("\n___Funcion que imprime un OCTOGONO___\n")
lado = int(input("Ingrese la longitud de un lado: "))
# Dibuja la primera parte
for a in range(lado):
    for b in range(lado-a):
        print(" ",end="")
    for c in range(lado+a*2):
        print("#",end="")
    print("")
# Dibuja la parte media
for a in range(lado-2):
    print(" ",end="")
    for b in range(lado+(lado-1)*2):
        print("#",end="")
    print("")
# diuja la ultima parte
for a in range(lado):
    for b in range(a+1):
        print(" ",end="")
    # print("")
    for c in range(lado*3-a*2-2):
        print("#",end="")
    print("")
    