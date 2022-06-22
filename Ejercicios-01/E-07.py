# EJERCICIO 7
# dado los numeros:
numeros = [1, 2, 5, 9, 12, 15, 17, 19, 21, 39, 45]
# indicar cuantos de ellos son multiplos de 3 y de 5 , ademas si hay un multiplo de 3 y de 5 no contabilizarlos
# multiplos de 3: 3 , multiplos de 5: 1
count_mult_3=0
count_mult_5=0
for a in range(len(numeros)):
    if (numeros[a]%3==0)and(numeros[a]%5==0):
        continue
    if numeros[a]%3==0:
        count_mult_3+=1
    if numeros[a]%5==0:
        count_mult_5+=1
print(count_mult_3,"son los numeros divisibles por 3.")
print(count_mult_5,"son los numeros divisibles por 5.")