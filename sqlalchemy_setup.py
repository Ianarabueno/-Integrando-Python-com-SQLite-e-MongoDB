from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Cliente(Base):
    __tablename__ = 'clientes'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    # Outros campos do cliente, se houver

    contas = relationship('Conta', back_populates='cliente')

class Conta(Base):
    __tablename__ = 'contas'

    id = Column(Integer, primary_key=True)
    numero = Column(String)
    saldo = Column(Integer)
    cliente_id = Column(Integer, ForeignKey('clientes.id'))

    cliente = relationship('Cliente', back_populates='contas')

# Criação do banco de dados e tabelas
engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

# Inserção de dados de exemplo
Session = sessionmaker(bind=engine)
session = Session()

# Cliente 1
cliente1 = Cliente(nome='Cliente A')
conta1 = Conta(numero='123456', saldo=1000)
cliente1.contas.append(conta1)

# Cliente 2
cliente2 = Cliente(nome='Cliente B')
conta2 = Conta(numero='654321', saldo=500)
cliente2.contas.append(conta2)

session.add_all([cliente1, cliente2])
session.commit()

# Exemplo de recuperação de dados
clientes = session.query(Cliente).all()
for cliente in clientes:
    print(f"Cliente: {cliente.nome}")
    for conta in cliente.contas:
        print(f"Conta: {conta.numero}, Saldo: {conta.saldo}")
