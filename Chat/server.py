import socket
import threading

HOST = '127.0.0.1'
PORT = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

salas = {}

def broadcast(sala, m):
    for i in salas[sala]: #percorrendo as pessoas na sala
        if isinstance(m, str):
            m = m.encode()
        
        i.send(m)
        
def enviarMsg(nome, sala, client):
    while True: #ficar escutando a sala
        mens = client.recv(1024)
        mens = f'{nome}: {mens.decode()}\n'
        broadcast(sala, mens)

while True: #tread de conexão
    client, addr = server.accept()
    client.send(b'SALA')
    sala = client.recv(1024).decode()
    nome = client.recv(1024).decode()
    if sala not in salas.keys():
        salas[sala] = []
    
    salas[sala].append(client)
    print(f'{nome} se conectou na sala {sala}! INFO {addr}\n')    
    #recebeu a mensage, agora enviar para todo mundo na sala! - broadcast
    broadcast(sala, f'{nome} entrou na sala!\n')
    thread = threading.Thread(target = enviarMsg, args = (nome, sala, client)) #para não executar um while dentro de outro
    thread.start()