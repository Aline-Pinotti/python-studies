from controller import *

while True:
    print("============================= [MENU] =============================")
    op = int(input('\t(1) Cadastrar;\n\t(2) Logar;\n\t(0) Sair.\n'))
    
    match op:
        case 1:
            nome = input("Nome: ")
            email = input("e-Mail: ")
            senha = input("Senha: ")
            r = Controller_Cadastro.cadastrar(nome, email, senha)
            
            match r:
                case 1:
                    print('Cadastro efetuado com sucesso!')
                case 2:
                    print('Tamanho do nome digitado inválido!')
                case 3:
                    print('O e-mail deve ter menos que 200 caracteres!')
                case 4:
                    print('A senha deve conter entre 6 e 100 caracteres!')
                case 5:
                    print('e-Mail já cadastrado!')
                case 6:
                    print('Erro interno do sistema.')
                case __:
                    pass
        
        case 2:
            email = input("e-Mail: ")
            senha = input("Senha: ")
            r = Controller_Login.login(email, senha)
            
            if not r:
                print('E-mail ou senha inválidos!')
            else:
                print(r)
                    
        case 0:
            break;
        
        case __:
            print('Opção inválida!\n')