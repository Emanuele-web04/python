fruits = ["apple", "banana", "mango"]

for fruit in fruits:
    print(fruit)

#how to add a new element to the end of a list
fruits.append("strawberry")
for fruit in fruits:
    print(fruit)

#change the middle fruit
fruits[2] = "blueberry"
for fruit in fruits:
    print(fruit)

# counting the elements of a list
for x in range(len(fruits)):
    x += 1
    print(x)