import socket

HOST = 'localhost'
PORT = 8002

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #informando o protocolo utilizado: TCP/IP
sock.bind((HOST, PORT)) #informar na tupla onde está sendo rodado
sock.listen(5) #quantos clientes vou escutar

while True:
    novoSock, _ = sock.accept() # ele retorna duas variáveis, mas como só vou usar uma, anonimizo a outra com _
    
    '''msg = novoSock.recv(1024).decode() #tamanho (em bytes)
    #msg vai retornar em binário, usa decode para decodificar (converter binário em string)
    print(msg)'''
    
    nomeArquivo = novoSock.recv(1024).decode()
    novoArquivo = novoSock.recv(1000000000)
    
    with open(f'arquivos/{nomeArquivo}', 'wb') as arq:
        arq.write(novoArquivo)
    
    novoSock.send(b'ok')