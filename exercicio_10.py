import math
ladoA=float(input("insira o lado a do triangulo:"))
ladoB=float(input("insira o lado b do triangulo:"))

ladoC= (ladoA**2 + ladoB**2)
ladoC2= math.sqrt(ladoC)

print("valor de hipotenusa:", ladoC2)
