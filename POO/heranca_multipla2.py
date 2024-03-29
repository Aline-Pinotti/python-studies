class Animal:
    def andar(self):
        print('Andando...')
    
    def correr(self):
        print('Correndo...')
        
    def pular(self):
        print('Pulando...')
    

class Felino():
    def ronronar(self):
        print('Prrrr')

    def ignorar(self):
        print('¬¬')
        
    def andar(self):
        print('Desfilando...')
        
class Gato(Felino, Animal): # a ordem é importante, pois se encontrar o método na primeira classe (felino) para de procurar (dá preferencia em chamar o andar da primeira classe - Felino)
    def miar(self):
        print('Miaauuu')
        

class Cachorro(Animal):
    def latir(self):
        print('Au-au')
        
        
frida = Gato()
frida.andar()