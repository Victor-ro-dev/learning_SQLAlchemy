from infra.configs.connection import DBConnectionHandler
from infra.entities.atores import Atores
from infra.entities.filmes import Filmes

class AtoresRepository:
    def select(self):
        with DBConnectionHandler() as db_connection:
            data = db_connection.session.query(Atores).all()
            result = [(ator.nome, ator.filme.ano) for ator in data]
            return result
        
    def insert(self, nome, titulo_filme):
        with DBConnectionHandler() as db_connection:
            try:
                db_connection.session.add(Atores(nome = nome, titulo_filme = titulo_filme))
                db_connection.session.commit()
            except Exception as e:
                db_connection.session.rollback()
                raise e


    def delete(self, nome):
        with DBConnectionHandler() as db_connection:
            db_connection.session.query(Atores).filter(Atores.nome == nome).delete()
            db_connection.session.commit()

    def update(self, nome, titulo_filme):
        with DBConnectionHandler() as db_connection:
            db_connection.session.query(Atores).filter(Atores.nome == nome).update({'titulo_filme': titulo_filme})
            db_connection.session.commit()