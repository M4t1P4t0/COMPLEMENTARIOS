n=int(input("Ingrese un número:"))
verificador = 0

for i in range(2, n):
    if n % i == 0 :
        verificador = verificador + 1

if verificador == 0:
    print (n, " Es un número primo")
else:
    print (n, " No es un número primo")