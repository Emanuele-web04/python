# do and catch in swift with try
text = input("Username: ")

try:
    number = int(text)
    print(number)
except:
    print("Nope")