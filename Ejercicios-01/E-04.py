# Conjetura de Collatz
print("\n___Conjetura de Collatz___")
val=int(input("Ingrese el numero a operar: "))
print("")
print(val,"",end="")
while val!=1:
    if val%2==0:
        val=int(val/2)
        print(val,"",end="")
    else:
        val=int(val*3+1)
        print(val,"",end="")
print("")