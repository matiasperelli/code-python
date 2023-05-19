from math import sqrt
op = float(input("Ingrese un valor para el cateto opuesto: "))
ad = float(input("Ingrese un valor para el cateto adjacente: "))
print("La hipotenusa es: " + str((round(sqrt(op**2+ad**2),3))))
