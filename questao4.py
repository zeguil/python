# Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.

pop_a = float(input("Digite a população do país A:  "))
pop_b = float(input("Digite a população do país B:  "))
tax_a = float(input("Digite a taxa de crescimento do país A: "))
tax_b = float(input("Digite a taxa de crescimento do país B: "))

ano = 0

while (pop_a < pop_b):
	pop_a += round((pop_a  *tax_a)/100)
	pop_b += round((pop_b * tax_b)/100)
	ano += 1

print("\nLevará", ano, "anos para população da cidade A ser maior que a cidade B\n")
print("população B:", pop_b, "habitantes")
print("população A:", pop_a, "habitantes")
