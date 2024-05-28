for i in range(0, 10, 1): #basically this is like for(int i = 0; i < 10; i++)
    print(i)

while 1:
    print(1) #infinite loops
    break #no more infinite 

loop = True
while loop:
    stop = input("Insert 'stop': ")
    if stop == "stop":
        loop = False