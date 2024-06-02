
import uuid
from classes import Anime
from classes import Animes

# user object
class User:

    def __init__(self, name, surname, listOfAnime = [], id = uuid.uuid4) -> None:
        self.name = name
        self.surname = surname
        self.listOfAnime = listOfAnime

    def changeStatus(self, newStatus = 1):
        anime = Anime()
        anime.setStatus(newStatus)


        