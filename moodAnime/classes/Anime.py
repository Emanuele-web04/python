 
# anime class

class Anime:

    def __init__(self, name: str, seen: bool = False) -> None:
        self.name = name
        self.seen = seen

    def getName(self) -> str:
        return self.name
    
    def getSeen(self) -> bool:
        return self.seen
    
    def setName(self, newName: str) -> None:
        self.name = newName
    
    def setSeen(self, isSeen: bool) -> None:
        self.seen = isSeen