# Dibujar un triangulo invertido
print("\n___Este programa imprime una triangulo invertido____\n")
lado=int(input("Ingrese el lado del triangulo (de preferencia impares): "))
print("")
pivot=int((lado+1)/2)
for a in range(pivot):
    for b in range(a):
        print(" ",end="")
    for c in range(lado-a*2):
        print("#",end="")
    print("")