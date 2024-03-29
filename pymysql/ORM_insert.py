from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ORM_create import Pessoa

def retornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = 3306
    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

    engine = create_engine(CONN, echo=True) #mostra mensagens se true, se false apenas mostra as mais importantes
    Session = sessionmaker(bind=engine) #posso criar mais de uma sessão para o mesmo banco de dados
    return Session()

session = retornaSession()

x = Pessoa(nome = 'Vincius',
           usuario = 'vinicius',
           senha='5678')

y = Pessoa(usuario = 'blksmth',
           senha = '123')

#session.add(x) #insere 1
session.add_all([x, y])#insere todos
#session.rollback() #desfazer as alterações
session.commit()