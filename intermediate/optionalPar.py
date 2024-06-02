
# setting a parameter = to something becomes automatically optional, 
# because it has a default value and you can call the func without inserting anything
def func(x = 1):
    return x**2

call = func()
print(call)

def freq(word = "Hello", add = 5, freq = 1):
    print(word * (freq + add))

display = print(freq("tim", 5))