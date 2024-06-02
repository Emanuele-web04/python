
# lambda functions
func2 = lambda x: x + 5
# onest m fa caca

def func(x):
    # it's handy when you have to create small functionality in a contained function, 
    # so you dont have to create a new one
    func2 = lambda x: x + 5
    return func2(x) + 85

a = [1,2,3,4,5,6,7,8,9,10]

# add 5 to each element of the array to the even numbers
newList = list(filter(lambda x: x % 2 == 0, a))
mappedList = map(lambda x: x + 5, newList)
print(list(mappedList))