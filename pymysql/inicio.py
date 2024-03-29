import pymysql.cursors

try:
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        port=3306, #3306 é a padrão, então não precisava passar
        db="aulapythonfull", #igual ao useaulapythonfull
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
except Exception as e:
    print(f'Problemas ao conectar no servidor de banco de dados: {e}')
       
def criaTabela(nomeTabela):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f'create table {nomeTabela} (nome varchar(50))')
            print(f'Tabela {nomeTabela} criada com sucesso!')
    except Exception as e:
        print(f'Problemas ao criar tabela {nomeTabela}: {e}')

def excluirTabela(nomeTabela):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f'drop table {nomeTabela}')
            print(f'Tabela {nomeTabela} ecluída com sucesso!')
    except Exception as e:
        print(f'Problemas ao excluir a tabela {nomeTabela}: {e}')

def insere(nomeTabela, *info):
    try:
        with connection.cursor() as cursor:
            for i in info:
                cursor.execute(f"insert into {nomeTabela} values('{i}')")
                print(f'{i} inserido na {nomeTabela} com sucesso!')
    except Exception as e:
        print(f'Problemas ao inserir na tabela {nomeTabela}: {e}')
        
def busca():
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"select * from teste")
            return cursor.fetchall()
    except Exception as e:
        #print(f'Problemas ao inserir na tabela {nomeTabela}: {e}')
        return None
        
#for i in busca():
#    print(i['nome'])

def alterar(alterar, novo):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"update teste set nome = '{novo}' where nome = '{alterar}'")
        print('Alterado com sucesso!')
    except Exception as e:
        print(f'Problemas ao fazer alteração: {e}')
        
def deletar(where):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"delete from teste where nome = '{where}'")
        print('Removido com sucesso!')
    except Exception as e:
        print(f'Problemas ao deletar: {e}')
        
insere('teste', 'aline', 'flávia', 'vinicius', 'zero')

connection.close()
