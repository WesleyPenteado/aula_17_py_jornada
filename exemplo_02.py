from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String


# Conectar ao SQLite em memória
engine = create_engine('sqlite:///meubanco.db', echo=True)

print("Conexão com SQLite estabelecida.")

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    idade = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

print("Tabela Criada com SQLite estabelecida.")

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

with Session() as session:
    novo_usuario = Usuario(nome='Ana', idade=25)
    session.add(novo_usuario)
    session.commit()

print("Usuário inserido com sucesso.")

usuario = session.query(Usuario).filter_by(nome='Ana').first()
print(f"Usuário encontrado: {usuario.nome}, Idade: {usuario.idade}")

