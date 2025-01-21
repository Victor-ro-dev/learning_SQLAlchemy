from infra.configs.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Filmes(Base):
    __tablename__ = 'filmes'

    titulo = Column(String(100), primary_key=True)
    genero = Column(String(100), nullable=False)
    ano = Column(Integer, nullable=False)
    atores = relationship("Atores", back_populates="filmes", lazy='select')

    def __repr__(self):
        return f"Filme(titulo={self.titulo}, genero={self.genero}, ano={self.ano})"