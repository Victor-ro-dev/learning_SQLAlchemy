from infra.repository.filmes_reposiory import FilmesRepository
from infra.repository.atores_repository import AtoresRepository
from time import sleep

repo_film = FilmesRepository()
repo_actor = AtoresRepository()

data = repo_actor.select()

print(data)