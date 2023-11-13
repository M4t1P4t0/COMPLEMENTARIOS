cantidad = 0
cantidadcar =int(input("Cuantos caracter quiere ingresar?"))
print("Ingrese ",cantidadcar," caracteres: ")

for i in range(0, cantidadcar):
    caracter = input("Ingrese Caracter: ")
    if caracter == "a" :
        cantidad = cantidad + 1
print ("En", cantidadcar, "caracteres hay", cantidad, "de  'a'")