from src.lib.loginUtils import HandlerJson
from os.path import dirname,realpath,join
from getpass import getpass
from passlib.hash import pbkdf2_sha256

class Login(HandlerJson):
    def __init__(self):
        self.root = dirname(realpath(__file__))
        self.pathData = join(self.root,'data/data.json')

    def main(self):
        print('------------- Bem-Vindo -------------')
        option = int(input('informe sua opção: 1 - cadastrar | 2 - Login: \n'))

        while option < 1 or option > 2:
            option = int(input('informe sua opção: 1 - cadastrar | 2 - Login'))


        if option == 1:
            self.signUp()
        else:
            self.signIn()
            

    def signUp(self):
        print('------------- Sign-Up -------------')
        username = input('Entre com nome do usuário: ')
        email = input('Entre com seu e-mail: ')
        password = getpass('Informe sua senha: ')
        passwordConfirm = getpass('Confirme sua senha: ')

        while password != passwordConfirm:
            print('Senha não confirmada! ')
            passwordConfirm = getpass('Confirme sua senha: ')
        
        HandlerJson().writeJson(self.pathData,username,email,pbkdf2_sha256.hash(passwordConfirm))

    def signIn(self):
        print('------------- Sign-In -------------')
        username = input('Entre com nome do usuário: ')
        password = getpass('Informe sua senha: ')

        

        data = HandlerJson().readJson(self.pathData)

        if (data['username'] == username):
            
            if pbkdf2_sha256.verify(password,data['password']):
                print('Usuario logado')
            else:
                print('Usuário sem permisão ou não encontrado') 
        else:
            print('Usuário sem permisão ou não encontrado')


if __name__ == '__main__':
    teste = Login()
    teste.main()