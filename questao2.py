#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 16 e 110;
#Salário: maior que zero;
#Sexo: femenino ou masculino;
#Estado Civil: 's', 'c', 'v', 'd';

nome = input(" Digite seu nome: ")

while len(nome) < 4:
    print ('\n##############################################')
    print ("ERROR: O nome deve ter mais de 3 caracteres. #")
    print ('##############################################\n')
    nome = input(" Digite seu nome: ")
print ("\n# Nome Salvo #\n")

idade = int(input(" Digite sua idade: "))

while (idade > 110 or idade < 16):
    print ('\n#########################################')
    print ("ERROR: a idade deve ser entre 16 e 110. #")
    print ('#########################################\n')
    idade = int(input(" Digite sua idade: "))

print ("\n# Idade Salva #\n")

sexo = int(input('Digite 1 se for do sexo masculino\nDigite 2 se for do sexo feminino\nResposta: '))
while (sexo != 1 and sexo != 2):
    print ('\n########################')
    print ('ERROR: opção invalida. #')
    print ('########################\n')
    sexo = int(input('Digite 1 se for do sexo masculino\nDigite 2 se for do sexo feminino\nResposta: '))

print ('\n# SEXO SALVO #\n')


est_civil = input('Digite a inicial do seu estado civil.\n"S" para solteiro.\n"C" para casado.\n"V" para viuvo.\n"D" para divorcidado.\nRESPOSTA: ')
while (est_civil != "s" and est_civil != "c" and est_civil != "v" and est_civil != "d"):
    print ('\n########################')
    print ('ERROR: opção invalida. #')
    print ('########################\n')
    est_civil = input('Digite a inicial do seu estado civil.\n"S" para solteiro.\n"C" para casado.\n"V" para viuvo.\n"D" para divorcidado.\nRESPOSTA: ')
if est_civil == 's':
    print ('\n# ESTADO CIVIL SALVO: SOLTEIRO')
elif est_civil == 'c':
    print ('\n# ESTADO CIVIL SALVO: CASADO')
elif est_civil == 'v':
    print ('\n# ESTADO CIVIL SALVO: VIUVO')
elif est_civil == 'd':
    print ('\n# ESTADO CIVIL SALVO: DIVORCIADO')

salario = float(input('\nDigite o salario: '))
while (salario < (1)):
    print ("\nERROR: salario não pode ser menor que 0")
    salario = float(input('\nDigite o salario: '))
print ("\n# SALARIO SALVO #\n")
print ('\n\n#############################\n\n')

print ("Seu nome é: ", nome)
print ("Sua idade é: ", idade)

if sexo == 1:
    print ('Seu sexo é: masculino')
else:
    print ('Seu sexo é: feminino')

if est_civil  == 's':
    print ('Seu estado civil é: solteiro')
elif est_civil  == 'c':
    print ('Seu estado civil é: casado')
elif est_civil  == 'd':
    print ('Seu estado civil é: divorciado')
elif est_civil  == 'v':
    print ('Seu estado civil é: viuvo')

print ('Seu salario é:', salario)

