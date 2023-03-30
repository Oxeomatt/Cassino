from time import sleep

# Criação de usuario e Senha
def account_creation():
    def new_login():
        with open('usuarios.txt', 'a') as arquivo:
            arquivo.write('\n{}'.format(new_account))

    def new_password():
        with open('senhas.txt', 'a') as arquivo:
            arquivo.write('\n{}'.format(new_account_password))

    def account_login():
        access_login = input(str('Logar no usuario criado? [sim] ou [nao]:  '))
        if access_login == 'sim':
            sleep(2)
            print('\nUsuario Logado!\n')

        elif access_login == 'nao':
            exit()


    print('Bem vindo ao Cassino do matt \n\n')
    new_account = input(str('Login: '))
    new_login()

    new_account_password = input(str('Agora digite uma senha: '))
    new_password()
    account_login()

