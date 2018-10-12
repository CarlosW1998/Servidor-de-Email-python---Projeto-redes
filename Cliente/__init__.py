import socket

HOST = 'localhost'
PORT = 12000

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)
print("Cliente Conectado")

while True :
    k = input()
    tcp.send(k.encode('utf8'))
    k = tcp.recv(4096)
    k = k.decode("utf8")
    print(k)
    if k == 'End':
        tcp.close()
        break
