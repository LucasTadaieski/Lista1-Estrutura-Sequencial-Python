'''
Elaborar um programa que calcule o salário líquido de um funcionário, exibindo no final o nome,
telefone e o salário líquido, considerando:
a) os dados do funcionário: nome, RG e telefone
b) salário bruto de R$ 2500,00
c) descontos de R$ 300,00.
'''

nome = input("Digite o seu nome: ")
rg = input("digite o seu RG: ")
telefone = input("digite o seu telefone: ")

salarioLiquido = 2500.0 - 300.0
 
#print("Nome: {}, telefone: {} e salário líquido: R${} ".format(nome, telefone, salarioLiquido))

print("Nome:", nome)
print("RG:", rg)
print("Telefone:", telefone)
print("salario liquido: R$", salarioLiquido)