
from classes import Anime

# class of animes, public
class Animes:

    def __init__(self, li = []) -> None:
        self.li = li

    def getList(self):
        return self.li
    
    def setList(self):
        li = [Anime("Berserk"), Anime("Dragon Ball"), Anime("Jujutsu Kaisen"), Anime("Bunny girl senpay"), Anime("AOT")]