from model import Pessoa
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

def retorna_session():
    CONN = "sqlite:///projeto2.db"
    engine = create_engine(CONN, echo = True)
    Session = sessionmaker(bind = engine)
    return Session()

class Controller_Cadastro():
    # vai faltar expressões regulares
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) > 50 or len(nome) < 3:
            return 2
        if len(email) > 200:
            return 3
        if len(senha) > 100 or len(senha) < 6:
            return 4
        
        return 1
    
    @classmethod
    def cadastrar(cls, nome, email, senha):
        session = retorna_session()
        
        usuario = session.query(Pessoa).filter(Pessoa.email == email).all() #busca os usuários com o e-mail informado, pra garantir não salvar e-mail repetido
        #se encontrar, não permite cadastrar com mesmo e-mail.
        if len(usuario) > 0:
            return 5 #e-mail já cadastrado
        
        dados_verificados = cls.verifica_dados(nome, email, senha)
        
        if dados_verificados != 1:
            return dados_verificados
        
        try:
            #encriptografando a senha
            senha = hashlib.sha256(senha.encode()).hexdigest() #encode transforma a string em binário (type byte), hexdigest transforma em hexadecimal
            p1 = Pessoa(nome=nome, email = email, senha = senha)
            session.add(p1)
            session.commit()
            return 1
        except:
            return 6
        
class Controller_Login():
    @classmethod
    def login(cls, email, senha):
        session = retorna_session()
        senha = hashlib.sha256(senha.encode()).hexdigest() #encriptografando a senha informada, pois iremos comparar as informações encriptografadas
        logado = session.query(Pessoa).filter(Pessoa.email == email).filter(Pessoa.senha == senha).all() #embora só vai ter 1
        
        if len(logado) == 1: #se deu certo o login...
            return {'logado': True, 'id' : logado[0].id}
        else:
            return False