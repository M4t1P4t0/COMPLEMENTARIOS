cantidadempleados=int(input ("Ingrese la cantidad de empleados:"))

i = 1
sueldomayor = 0

print("Ingrese los sueldos: ")
while i <= cantidadempleados :
    sueldo = float( input("Ingrese sueldo {0}: ".format(i)))
    if sueldo > sueldomayor :
        sueldomayor = sueldo
    c = i
    i = i + 1

print ("El empleado numero ", c, "tiene el mayor sueldo que es:", sueldomayor)