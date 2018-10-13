from BDoperations import *
import _thread
#Todas as mensagens são textos codificados em bytes

def conection(con, addr):
    print("Begin of trasmitions")
    while True :
        #Aqui o servidor apenas pega a conexão do clien e decodifica
        #O servidor usa / como separador para as partes da mensagem
        mensage = con.recv(4096)
        mensage = mensage.decode("utf8")
        print("Recive from ",addr, end = '')
        print(" " + mensage)
        mensage = list(mensage.split('/'))

        #Aqui começa o tratamento Das mensagens enviadas
        #End siginifica o fim da conexão
        if mensage[0] == 'End':
            con.send("End".encode())
            break


        #Aqui estãos as consultas Get ao servidor
        elif mensage[0] == 'GET':
            if len(mensage) == 1 :
                con.send("DadoInvalido".encode())
            elif mensage[1] == 'TOKEN':
                con.send("Envie seu email e senha".encode())
                data = con.recv(4096)
                data = data.decode('utf8')
                data = list(data.split("/"))
                con.send(getToken(data).encode())
            elif mensage[1] == 'EMAIL':
                con.send("Send token, and email id".encode())
                data = con.recv(1024).decode()
                data = list(data.split("/"))
                con.send(getEmail(data).encode())
            elif mensage[1] == 'EMAILS':
                con.send("SEND TOKEN".encode())
                token = con.recv(1024).decode()
                con.send(getEmails(token).encode())
            else : con.send("Mensagem Invalida".encode())


        #Funçoes de POST
        elif mensage[0] == 'POST':
            if len(mensage) == 1 :
                con.send("DadoInvalido".encode())
            elif mensage[1] == 'USER':
                con.send("Send Name, Email and passwor".encode())
                data = con.recv(4096).decode()
                data = list(data.split('/'))
                con.send(addUser(data).encode())
            elif mensage[1] == 'EMAIL':
                con.send("Send token, context, mensage and target".encode())
                data = con.recv(4096).decode()
                data = list(data.split("/"))
                con.send(SendEmail(data).encode())
            else : con.send("Mensagem Invalida".encode())

        #Deletando emails
        elif mensage[0] == 'DELETE':
            if len(mensage) == 1 :
                con.send("DadoInvalido".encode())
            elif mensage[1] == 'EMAIL':
                con.send("Send token, and email id".encode())
                data = con.recv(1024).decode()
                data = list(data.split("/"))
                con.send(deleteEmail(data).encode())
            else: con.send("Mensagem Invalida".encode())


        else :con.send("Mensagem Invalida".encode())


    #Fim da conexão
    con.close()
    print('End of trasmissions')
    _thread.exit()