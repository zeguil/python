print('E necessario ter informaçoes para entrar no exercito\n')

peso=input('Digite seu peso: ')
idade=input('\nDigite sua idade: ')
altura=input('\nDigite sua altura: ')

if peso >= '70' and idade >= '18' and altura >= '1.70':
    print('\nvoce esta APROVADO')
else:
    print('\nvoce esta REPROVADO')