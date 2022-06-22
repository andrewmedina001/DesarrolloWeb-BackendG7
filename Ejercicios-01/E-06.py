num_aleatorio=int(input("Ingrese un numero: "))
num_adivinar=3
while(num_adivinar!=num_aleatorio):
    if num_aleatorio<num_adivinar:
        print("El numero es mayor")
    elif num_aleatorio>num_adivinar:
        print("El numero es menor")
    else:
        print("!Adivinaste el numero¡")
    num_aleatorio=int(input("Ingrese otro numero: "))
    if num_aleatorio==num_adivinar:
        print("!Adivinaste el numero¡")