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
