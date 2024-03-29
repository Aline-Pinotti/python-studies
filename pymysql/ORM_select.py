from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker
from ORM_create import Pessoa

def retornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = 3306
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=False) #mostra mensagens se true, se false apenas mostra as mais importantes
    Session = sessionmaker(bind=engine) #posso criar mais de uma sessão para o mesmo banco de dados
    return Session()

session = retornaSession()

pessoa = session.query(Pessoa).all() #retorna uma list de objetos Pessoa
print('todos os registros', pessoa[0].nome)

pessoa2 = session.query(Pessoa).filter(Pessoa.nome == 'aline')
print('filtrando apenas um atributo (nome)', pessoa2[0].nome)

pessoa3 = session.query(Pessoa).filter(Pessoa.usuario == 'aline').filter(Pessoa.senha == '1234').all() #sem .all() retorna o sql, com .all() retorna a lista
print('filtrando mais de um atributo (and)', pessoa3[0].nome)

pessoa4 = session.query(Pessoa).filter_by(usuario = 'aline', senha = '1234').all()
print('outra forma de fazer (filter_by)', pessoa4[0].nome)


pessoa5 = session.query(Pessoa).filter(or_(Pessoa.nome == 'aline', Pessoa.nome == 'Vincius')).all()
for i in pessoa5:
    print(i.nome)
    
    
#UPDATE
pessoa = session.query(Pessoa).filter(Pessoa.id == 2).all()
pessoa[0].nome = 'vinicius'
session.commit()

#DELETE
pessoa = session.query(Pessoa).filter(Pessoa.id == 3).delete()
session.commit()

#outra forma de se fazer

#pessoa = session.query(Pessoa).filter(Pessoa.id == 4).all() #traz a lista
#session.delete(pessoa[0]) #não é a melhor forma de se fazer

pessoa = session.query(Pessoa).filter(Pessoa.id == 4).one() #traz apensa um objeto
session.delete(pessoa)
session.commit()