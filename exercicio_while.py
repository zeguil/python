# Criar um programa que leia o numero de convidados de uma festa, 
# depois leia o nomes dos convidados e emprima em uma lista 

numero_p = input ('digite o numero de convidados: ')
lista_conv = []
i = 1
while i <= int(numero_p):
    nome_conv = input('digite o nome do convidado #' + str(i) +': ')
    lista_conv.append(nome_conv)
    i += 1

for convidado in lista_conv:
    print(convidado)