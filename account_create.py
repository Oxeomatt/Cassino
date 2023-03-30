from time import sleep

# Criação de usuario e Senha
def account_creation():
    def new_login():
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write('\n{}'.format(new_account))

    def new_password():
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write('\n{}'.format(new_account_password))
            sleep(2)
            print('\nUsuario criado com sucesso! ')


    print('Bem vindo ao Cassino do matt \n\n')
    new_account = input(str('Login: '))
    new_login()

    new_account_password = input(str('Agora digite uma senha: '))
    new_password()
 

