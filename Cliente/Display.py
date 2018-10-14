from Cliente.Consult import ServerConect

class Dysplay:
    def __init__(self):
        self.conection = ServerConect()
        self.token = None
        self.err = {'101' : 'Falha ao conectar ao banco de dados', '202' : 'Dados Invalidos' , '303' : 'Token Invalido', '505' : 'Usuario ja existe', '606' : 'usuario invalido', '707' : 'Mensagem invalida'}

    def execute(self):
        while True:
            print("1 para entrar no sistema -1 para sair")
            k = input()
            while k != '1' and k != '-1':
                print("Entrada invalida")
                k = input()
            if k == '-1': break
            self.conection.openConection()
            condition = True
            while condition:
                print("1 para logar, 2 para criar um usuario ")
                option = input()
                if option == '1':
                    result = self.showLogin()
                    token = self.conection.getToken(result[0], result[1])
                    if token in self.err.keys():
                        print(self.err[token])
                    else:
                        self.token = token
                        self.email = result[0]
                        condition = False
                elif option == '2':
                    print("Nome: ", end = '')
                    name = input()
                    print("Email: ", end = '')
                    email = input()
                    print("Senha: ", end = '')
                    senha = input()
                    print(self.creaateUser(name,  email, senha))

                else: print("Opção invalida")
            condition = True
            while condition:
                print('Bem vindo ', self.email)
                print('digite -1 para sair, 1 exibir os emails 2 para enviar um email e 3 para abrir um email, 4 para deletar um email')
                option = input()
                if option == '-1':
                    self.token = None
                    self.email = None
                    self.conection.closeConection()
                    condition = False
                elif option == '1': print(self.showEmails())
                elif option == '2':
                    print("Titulo: ", end = '')
                    title = input()
                    print('Mensagem: ', end = '')
                    mensage  =input()
                    print("Destinatario: ", end = '')
                    destinatario = input()
                    print(self.sendEmail(title, mensage, destinatario))
                elif option == '3':
                    print("Digite o numero do email: ", end = '')
                    id = input()
                    print(self.getEmail(id))
                elif option == '4':
                    print("Digite o numero do email: ", end = '')
                    id = input()
                    print(self.deleteEmail(id))
                else:print("Opcao invalida")

    def showLogin(self):
        print('Email: ', end = '')
        email = input()
        print('Senha: ', end = '')
        senha = input()

        return (email, senha)
    def showEmails(self):
        resullt = self.conection.getEmails(self.token)
        if resullt in self.err.keys():
            return self.err[resullt]
        return resullt

    def sendEmail(self, context, mensage, target):
        result = self.conection.postEmail(self.token, context, mensage, target)
        if result in self.err.keys():
            return self.err[result]
        return result
    def getEmail(self, id):
        result = self.conection.getEmail(self.token, id)
        if result in self.err.keys():
            return  self.err[result]
        return result
    def deleteEmail(self, id):
        result = self.conection.deleteEmail(self.token, id)
        if result in self.err.keys():
            return self.err[result]
        return result
    def creaateUser(self, nome, email, senha):
        result = self.conection.postUser(nome, email, senha)
        if result in self.err.keys():
            return self.err[result]
        return result