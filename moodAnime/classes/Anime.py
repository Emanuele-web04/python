 
# anime class
class Anime:

    def __init__(self, name, hasBeenSeen = 0) -> None:
        self.name = name
        self.hasBeenSeen = hasBeenSeen
    
    # get and set for hasBeenSeen
    def getStatus(self):
        return self.hasBeenSeen
    
    def setStatus(self, newStatus):
        self.hasBeenSeen = newStatus
    
