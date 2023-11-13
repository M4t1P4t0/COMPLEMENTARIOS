i = 0
c = 0
cantidadnum =int(input("Cuantos numeros quiere ingresar?"))
for i  in range(i, cantidadnum):
    n = int( input("Ingrese número: "))
    i = i + 1
    if n%2 == 0 :
        c = c + 1
        

print ("En", cantidadnum, " hay ", c, "números pares")