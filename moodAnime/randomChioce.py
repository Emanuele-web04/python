
# now here we combine everything

from classes import Animes
from classes import User 
from random import choice

animes = Animes()
listOfAnimes = animes.setList()

username = input()
userSurname = input()
user = User(username, userSurname, listOfAnimes)

print("Hello", username + userSurname)

print("These are the animes:\n")
for anime in listOfAnimes:
    print(anime)

print("Did you see some already? y or n")
response = input()

if response == "n":
    print("The anime we suggest is:", choice(listOfAnimes))
else:
    print("Insert the name of the anime you already saw")
    alreadySeen = input()
    found = listOfAnimes.find(alreadySeen)
    if found != -1:
        listOfAnimes.remove(listOfAnimes[found])
    print("The anime we suggest is:", choice(listOfAnimes))



