
limite = int( input("Ingrese la cantidad de números a comparar:"))
men = 999999999
may = 0
cont=1
for i in range(0, limite):
    n = int( input("Ingrese número: "))
    if n < men :
        men = n
    else:
        if n > may :
            may = n

print ("El menor es :",men)
print ("El mayor es :",may)