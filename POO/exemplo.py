#programação comum (que usamos pra aprender)
x = []                 #como estamos estreuturamos nosso raciocínio (sentido lógico)
for i in range(0, 10): # crio um laço de repetição, que passa por cada um dos valores
    if i % 2 == 0:     # passo por cada um dos valores e verifico se é par
        x.append(i)    # depois adiciono dentro da lista
        
        
#Utilizando List Comprehension -- programação funcional
x = [i for i in range(0, 10) if i % 2 == 0]

# Orientação de Objetos : não é tão poderosa como Java e C# -- não tem encapsulamento - não precisa primeiro criar classes antes de programar
# não é tão comum programar 100% orientado a objetos, costuma ser uma "salada de paradigmas"

# no POO Começamos com Objetos (modelagem de uma entidade) - trabalhando com seus dados
# Ex. Cadastro de pessoa: nome, rg, cpf et.. pessoa = entidade.. entao crio entidade chamada Pessoa que tem atributos(características) e métodos(ações)