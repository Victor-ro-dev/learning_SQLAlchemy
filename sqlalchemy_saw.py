from sqlalchemy import create_engine, text
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


# Corrija o nome do driver para 'pymysql' e atualize a porta se necessário
engine = create_engine('mysql+pymysql://root:Dravenak47@localhost:3306/cinema')
conn = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase):
    pass

class Filmes(Base):
    __tablename__ = 'filmes'

    titulo = Column(String(100), primary_key=True)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return f"Filme(titulo={self.titulo}, genero={self.genero}, ano={self.ano})"
    
data_insert = Filmes(titulo='Vingadores', genero='Ação', ano=2012)
session.add(data_insert)
session.commit()

session.query(Filmes).filter(Filmes.titulo == 'Vingadores').delete()

session.query(Filmes).filter(Filmes.titulo == 'Vingadores').update({'ano': 2012})
data = session.query(Filmes).all()
print(data)
