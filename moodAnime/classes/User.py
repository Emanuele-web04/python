
import uuid
import Anime

# user object
class User:

    # nella riga degli argomenti non inizializzare gli elementi mutabili
    def __init__(self, name: str, liAnime: list = None) -> None:
        self.id = uuid.uuid4() # da cercare
        self.name = name
        # se li non è null
        if liAnime:
            self.liAnime = liAnime
        else:
            self.liAnime = []
    
    def getID(self) -> uuid:
        return self.id

    def getName(self) -> str:
        return self.name
    
    def getList(self) -> list:
        return self.liAnime.copy()
    
    # setter
    def setName(self, newName: str):
        self.name = newName
    
    def setList(self, newList: list):
        self.liAnime = newList

    def setSeen(self, animeName):
        i = 0
        while i < len(self.liAnime) and self.liAnime[i].getName() != animeName:
            i += 1
        
        if i < len(self.liAnime):
            self.liAnime[i].setSeen(True)

    def appendAnime(self, newAnime: Anime):
        if not isinstance(newAnime, Anime):
            return
        self.liAnime.append(newAnime)

    def __str__(self) -> str:
        lines = []
        str_animes = ""
        for anime in self.liAnime:
            str_animes += ' ( ' + anime.getName() + ',' + str(anime.getSeen()) + ' ) '
        lines.append(f"{self.name} : {str_animes}")
        return '\n'.join(lines) 



        