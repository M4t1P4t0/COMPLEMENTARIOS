n=int(input ("Ingrese un numero: "))
resto = 0
contador=0
while n>0:
    resto=n % 10
    n=n//10
    
    if resto==0:
        contador=contador+1

print ("Hay ", contador, " números ceros")