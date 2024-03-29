import socket
#from time import sleep

HOST = '127.0.0.1'
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

msg = client.recv(1024)
if msg == b'SALA':
    client.send(b'Jogos')
    #sleep(1)
    client.send(b'Aline')