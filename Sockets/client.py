import socket

HOST = 'localhost'
PORT = 8002

arquivo = open('thumb.png', 'rb')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST, PORT)) #fazendo a conexão ao server
#sock.send(b'teste') #preciso convertes para bytes
sock.send(input().encode()) #preciso converter para bytes
sock.send(arquivo.read())

conf = sock.recv(1024)
if conf == b'ok':
    print('Mensagem recebida!')
    