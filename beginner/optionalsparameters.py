def func(x):
    print(x)

func(2)

def func(x, text = '3'): # this way you set a default value, unless you want to change it
    print(x)
    if text == "2":
        print("nice")
    else:
        print("ok no")

func(2)