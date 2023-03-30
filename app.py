from account_create import *
from time import sleep
from carteira import *


print('''
#################################################
             Cassino do Matt 1.0
#################################################
             
            1 - Logar
            2 - Criar conta
            3 - Exit
            ''')

app_menu = input(str('Digite uma das opções: '))


if app_menu == '1':
    account_login = input(str('Login: '))
    with open('usuarios.txt', 'r') as arquivo:
        usuario = arquivo.readlines()
        if account_login in usuario:
            account_password = input(str('Password: '))

            with open('senhas.txt', 'r') as senha:
                a_senha = senha.readlines()
                if account_password in a_senha:
                    sleep(2)
                    print('Logado com sucesso!')
                    sleep(2)
                    print('''
################################################################
#                   Cassino do Matt 1.0                        #
# Nome: {}                               Cash: R$ {}        #     
#                                                              #
################################################################                    
                    '''.format(account_login, "0"))
                    
                    

elif app_menu == '2':
    account_creation()

elif app_menu == '3':
    exit()