
# filter function
def add7(x):
    return x + 7

def isOdd(x):
    return x % 2 != 0

a = [1,2,3,4,5,6,7,8,9,10]

# same as map, is going to pass the function to a
# it's filtering objects base on a function we create
b = list(filter(isOdd, a))

# filter and map
# you add 7 just to the odd numbers
c = list(map(add7, b))