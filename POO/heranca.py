class Pessoa:
    def falar (self):
        print('Blá blá blá...')
    
    def andar(self):
        print('Step step step...')
        
    def rir(self):
        print('rsrs')
    
    def cascar_o_bico(self):
        print('Hasuhaushuas')
    
class Cliente(Pessoa):
    def comprar(self):
        print('À vista tem desconto?')

class Vendedor(Pessoa):
    def vender(self):
        print('Posso lhe ajudar?')
        
        
c1 = Cliente()

c1.andar()
c1.comprar()
c1.cascar_o_bico()