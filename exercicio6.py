salario = float(input("Digite o valor atual do salario: "))
percentualAumento = float(input("Digite o valor percentual do aumento: "))

aumento = salario * (percentualAumento / 100)
novoSalario = salario + aumento

print("O valor do aumento salarial é:", aumento)
print("O valor do novo salario é:", novoSalario) 