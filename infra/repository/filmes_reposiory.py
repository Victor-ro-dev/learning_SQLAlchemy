from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Filmes).all()
            return data
        
    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db_connection:
            db_connection.session.add(Filmes(titulo=titulo, genero=genero, ano=ano))
            db_connection.session.commit()

    def delete(self, titulo):
        with DBConnectionHandler() as db_connection:
            db_connection.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db_connection.session.commit()

    def update(self, titulo, ano):
        with DBConnectionHandler() as db_connection:
            db_connection.session.query(Filmes).filter(Filmes.titulo == titulo).update({'ano': ano})
            db_connection.session.commit()