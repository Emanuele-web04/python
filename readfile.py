file = open('file.txt', 'r') # r for "read"
f = file.readlines()

print(f)

newList = []
for line in f:
    if line[-1] == '\n':
        newList.append(line[:-1]) # goes to the last char but does not consider the last
    else:
        newList.append(line)
print(newList)

for line in f:
    newList.append(line.strip())
    
print(newList)