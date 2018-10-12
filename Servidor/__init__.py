import socket
import _thread
from Servidor.ClientConection import conection


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = ""
PORT = 12000

s.bind((HOST, PORT))
s.listen(1)

print("Servidor Conectado")


while True :
    con, addr = s.accept()
    _thread.start_new_thread(conection, (con, addr))
    #conection(con, addr)
    break
s.close()