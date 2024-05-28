string = "Helloaahahahahnjnjnjpiu"
print(string.find("ah")) # linear search basically
print(string.count("ah"))

# imma do my own thing
def find(string, letter):
    for x in range(len(string)):
        if letter == string[x]:
            return x
        
def count(string, letter):
    counter = 0
    for x in range(len(string)):
        if letter == string[x]:
            counter += 1
    return counter
        
print(find(string, "e"))
print(count(string, "a"))

