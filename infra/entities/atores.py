from infra.configs.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Atores(Base):
    __tablename__ = 'atores'

    id = Column(Integer, primary_key=True)
    nome = Column(String(100), nullable=False)
    titulo_filme = Column(String(100), ForeignKey('filmes.titulo'))

    def __repr__(self):
        return f"Ator(nome={self.nome}, titulo_filme={self.titulo_filme})"
  