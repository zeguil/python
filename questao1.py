# programa que lê um nome de usuário e a sua senha e não aceita a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações


usuario = input('Digite o nome de usuario: ')
senha =  input('Digite a senha: ')


while (senha == usuario):
    print('\nERROR: usuario e senha nao podem ser iguais!\n')
    usuario = input('digite o nome de usuario: ')
    senha =  input('digite a senha: ')

if (senha != usuario):
    print('\n#########################')
    print('Conta Criada Com Sucesso\n')
    print('SEU LOGIN É: ', usuario, '\nSUA SENHA É: ', senha)
