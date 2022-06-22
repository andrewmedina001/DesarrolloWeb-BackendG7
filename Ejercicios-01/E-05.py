# Ejercicio 05
# que separe el texto por los espacios
# y lo convierta en un arreglo
# y cada inicial este en mayuscula
print("")
txt="texto separado por espacios"
print("Texto Original--> \"",end="")
print(txt,end="")
print("\"")
txtPivot=txt.split(" ")
for a in range(len(txtPivot)):
    txtPivot[a]=txtPivot[a].capitalize()
print(txtPivot)
print("")