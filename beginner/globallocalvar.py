var = 9
loop = True

def func(x):
    newVar = 7

    if x == var:
        return newVar
    
# print(newVar) big bro the var is in the function, it's not global

newVar = func(var) #now you can
print(newVar)
