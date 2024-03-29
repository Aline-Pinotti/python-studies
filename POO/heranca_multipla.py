class Animal:
    def andar(self):
        print('Andando...')
    
    def correr(self):
        print('Correndo...')
        
    def pular(self):
        print('Pulando...')
    

class Felino(Animal):
    def ronronar(self):
        print('Prrrr')

    def ignorar(self):
        print('¬¬')
        
class Gato(Felino):
    def miar(self):
        print('Miaauuu')
        

class Cachorro(Animal):
    def latir(self):
        print('Au-au')
        
        
frida = Gato()
frida.pular()

dodo = Gato()
dodo.ignorar()

#Quanto menor sua cadeia de heranças melhor. Menor o risco de sobrepor o método. Evitar, se possível.