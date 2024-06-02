
# map function
# example without the map function

li = []

# i populate the list with a for
for i in range(10):
    li.append(i + 1)

print(li)

def tetraction(x):
    return x**x

# with map i want to calculate the tetration of every list element and save the values in a new list
# without map:
newList = []
for i in range(10):
    newList.append(tetraction(i + 1))

print(newList)

# with map
# map takes 2 para: func, list, the logic in the function is passed then into the list
print(list(map(tetraction, li)))

# list comprehension
# it's literally litteral
# you can even add conditions
print([tetraction(x) for x in li if x % 2 == 0])