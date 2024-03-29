class Pessoa:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf        
    
    def falar (self):
        print('Blá blá blá...')
    
    def andar(self):
        print('Step step step...')
        
    def rir(self):
        print('rsrs')
    
    def cascar_o_bico(self):
        print('Hasuhaushuas')
    
class Cliente(Pessoa):
    
    def __init__(self, id_cliente, nome, cpf):
        super().__init__(nome, cpf)
        self.id_cliente = id_cliente
    
    def comprar(self):
        print('À vista tem desconto?')
        
    def comprar(self):
        print('Parcela em quantas vezes sem juros?')

    def falar(self):
        super().falar() #referencia a classe pai, de forma a não sobrepor, mas sim complementar
        print('Ok :)')
        
c1 = Cliente(2, 'João da Silva', 12345678965)

'''c1.andar()
c1.comprar()
c1.cascar_o_bico()
c1.falar()'''

print(c1.id_cliente)
print(c1.nome)
print(c1.cpf)