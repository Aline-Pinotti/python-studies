from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USUARIO = "root"
SENHA = ""
HOST = "localhost"
BANCO = "aulapythonfull"
PORT = 3306
CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"

engine = create_engine(CONN, echo=True) #mostra mensagens se true, se false apenas mostra as mais importantes
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Pessoa(Base):
    __tablename__ = "pessoa" #possível utilizar porque herdamos de Base
    id = Column(Integer, primary_key=True)
    nome = Column(String(50)) #50 caracteres
    usuario = Column(String(20))
    senha = Column(String(10))
    
class Categoria(Base):
    __tablename__ = "categoria"
    id = Column(Integer, primary_key=True)
    categoria = Column(String(50))
    
class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True)
    produto = Column(String(50))
    #idCategoria = Column(Integer).foreign_keys(Categoria.id)
    idCategoria = Column(Integer, ForeignKey('categoria.id'))
    
Base.metadata.create_all(engine)