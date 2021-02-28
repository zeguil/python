# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

num1 = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))

lista = []

while (num2 < num1):
	print ("\n#  ERROR: primeiro numero deve ser maior que o segundo. #\n")
	num1 = int(input("digite um numero: "))
	num2 = int(input("digite outro numero: "))

for i in range(num1+1,num2,1):
	lista.append(i)

print(lista)
