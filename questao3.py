# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3%
# e que a população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
# Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B.

hab_a = 80000 
hab_b = 200000 

ano = 0
while (hab_a < hab_b):
    hab_a += round((hab_a * 3.0)/100)
    hab_b += round((hab_b * 1.5)/100)
    ano += 1
print("levará" , ano, "anos para população da cidade A ser maior que a cidade B")
print("HABITANTES A: ", hab_a, "habitantes")
print("HABITANTES B: ", hab_b, "habitantes")
