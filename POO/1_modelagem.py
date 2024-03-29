#1º passo, determinar quais Entidades vamos precisar. Vai depender do problema a ser resolvido
#
# especificar padrões que todas as entidades daquele objeto vai ter
    #PEP* 8: Guia de estilização do Python - Como deve criar o código de forma mais legível.
    #   Nomes de classes comecem com letras maiúsculas e, no caso de nome duplo, cada nome começa com a letra maiúscula. Ex.: class PessoasClientes:
    #   Nomes de funcoes são todos em letras minúsculas e, no caso de nome duplo, separados por _. Ex.: def cadastrar_pessoa:
# *PEPs: por onde o pessoal do python discute alguns padrões, regras - são as convensões.. existem mais de 500    
class Pessoas: # sem herança ()
    #ATRIBUTOS
    def __init__(self, pnome, pidade, pcpf): #dunder init dunder
        self.nome = pnome
        self.idade = pidade
        self.cpf = pcpf
        
    #METODOS (apenas uma instância desse Objeto pode chamar essa "função")
    def logar_sistema(self): # Segundo o PEP8 de estilização, os métodos seguem o mesmo padrão de nomenclatura que as funções
        print(f'{self.nome} logando no sistema')
        
#criando instância p1 do objeto Pessoas
p1 = Pessoas('Caio Sampaio', 21, '323456789')
p2 = Pessoas('Marcos Antônio', 25, '321654987')

p1.logar_sistema()
p2.logar_sistema()
