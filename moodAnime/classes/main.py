
# now here we combine everything
# Anime e User sono i singoli file
from Anime import Anime
from User import User
import uuid
import copy

userList = []
a1 = Anime("mha")
animeList = [Anime("jojo"), Anime("dragonball"), Anime("jjk"), Anime("bunny girl senpai")]

# add user function
def addUser(user: User):
    # mala copia di tutte l'anime list, quindi diventa suo (dell'utente), senza toccare il "main" list
    user.setList(copy.deepcopy(animeList))
    # aggiunto l'user con una nuova lista vuota
    userList.append(user)

def addAnime(anime: Anime):
    animeList.append(anime)
    for user in userList:
        user.appendAnime(copy.deepcopy(anime))

def displayUserList():
    for user in userList:
        print(user)

u1 = User("Giorgio")
u2 = User("Giacomo")

addUser(u1)
addUser(u2)
displayUserList()

u2.setSeen("jojo")
displayUserList()
addAnime(a1)
displayUserList()
