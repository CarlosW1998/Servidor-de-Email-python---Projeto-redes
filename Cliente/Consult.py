import socket

class ServerConect:

    def openConection(self):
        HOST = 'localhost'
        PORT = 12000
        self.tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        dest = (HOST, PORT)
        self.tcp.connect(dest)
        print("Cliente Conectado")
    def getToken(self, email, password):
        consult = "GET/TOKEN"
        self.tcp.send(consult.encode('utf8'))
        result = self.tcp.recv(4096).decode()
        if result == 'Envie seu email e senha':
            consult = email + '/' + str(password)
            self.tcp.send(consult.encode('utf8'))
            return self.tcp.recv(4096).decode()
        return 'FAIL'
    def getEmail(self, token, id):
        consult = "GET/EMAIL"
        self.tcp.send(consult.encode('utf8'))
        result = self.tcp.recv(4096).decode()
        if result == "Send token, and email id":
            consult = token + "/" + str(id)
            self.tcp.send(consult.encode('utf8'))
            return self.tcp.recv(4096).decode()
        return "FAIL"
    def getEmails(self, token):
        consult = 'GET/EMAILS'
        self.tcp.send(consult.encode('utf8'))
        result = self.tcp.recv(4096).decode()
        if result == 'SEND TOKEN':
            consult = token
            self.tcp.send(consult.encode('utf8'))
            return self.tcp.recv(4096).decode()
        return "FAIL"
    def postUser(self, name, email, password):
        consult = 'POST/USER'
        self.tcp.send(consult.encode('utf8'))
        result = self.tcp.recv(4096).decode()
        if result == 'Send Name, Email and passwor':
            consult =  name + '/' + email + '/' + str(password)
            self.tcp.send(consult.encode('utf8'))
            return self.tcp.recv(4096).decode()
        return "FAIL"
    def postEmail(self, token, context, mensage, target):
        consult = 'POST/EMAIL'
        self.tcp.send(consult.encode('utf8'))
        result = self.tcp.recv(4096).decode()
        if result ==  "Send token, context, mensage and target":
            consult = token  + "/" + context + '/' + mensage + '/' + target
            self.tcp.send(consult.encode('utf8'))
            return self.tcp.recv(4096).decode()
        return 'FAIL'
    def deleteEmail(self, token, id):
        consult = 'DELETE/EMAIL'
        self.tcp.send(consult.encode('utf8'))
        result = self.tcp.recv(4096).decode()
        if result == 'Send token, and email id':
            consult = token + '/' + str(id)
            self.tcp.send(consult.encode('utf8'))
            return  self.tcp.recv(4096).decode()
        return 'FAIL'
    def closeConection(self):
        self.tcp.send('End'.encode())
        self.tcp.close()