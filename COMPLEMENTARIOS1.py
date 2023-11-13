contador = 0
print("Ingrese 10 números: ")
for i in range(1, 10 + 1):
    num = int( input("Ingrese Número: "))
    if num % 2 == 0 :
        contador = contador + 1

print("Hay", contador, "números pares")