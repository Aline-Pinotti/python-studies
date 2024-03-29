import socket
import threading
from tkinter import *
import tkinter
from tkinter import simpledialog

class Chat:
    def __init__(self):
        
        HOST = '127.0.0.1'
        PORT = 55555

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((HOST, PORT))
        
        login = Tk()
        login.withdraw()
        
        self.janela_carregada = False
        self.ativo = True
        
        self.nome = simpledialog.askstring('nome', 'Digite seu nome: ', parent=login)
        self.sala = simpledialog.askstring('sala', 'Digite a sala que deseja entrar: ', parent=login)
        
        thread = threading.Thread(target=self.conecta)
        thread.start()
        
        self.janela()
    
    def janela(self): #responsável pela interface
        self.root = Tk()
        self.root.geometry('800x800')
        self.root.title('Chat')
        
        self.caixa_texto = Text(self.root)
        self.caixa_texto.place(relx=0.05, rely=0.01, width=700, height=600)
        
        self.envia_msg = Entry(self.root)
        self.envia_msg.place(relx=0.05, rely=0.8, width=500, height=20)
        
        self.btn_enviar = Button(self.root, text = 'Enviar', command=self.enviarMensagem)
        self.btn_enviar.place(relx=0.7, rely=0.8, width=100, height=20)
        
        self.root.protocol("WM_DELET_WINDOW", self.fechar)
        
        self.root.mainloop()
        
    def fechar(self):
        self.root.destroy()
        self.client.close()
        
    def conecta(self):
        while True:
            rec = self.client.recv(1024)
            if rec == b'SALA': #poderia ser usado algo como hash para não dar problema se envioarem a palavra "sala"
                self.client.send(self.sala.encode())
                self.client.send(self.nome.encode())
            else:
                try: #a primeira vez que tenta executar a caixa de texto não foi criada ainda
                    self.caixa_texto.insert('end', rec.decode())
                except:
                    pass
    
    def enviarMensagem(self):
        msg = self.envia_msg.get()
        self.client.send(msg.encode())
        self.envia_msg.delete(0, END)
        
        
chat = Chat()