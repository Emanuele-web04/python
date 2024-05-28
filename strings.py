text = input("Say sum:")
print(text.strip()) # this method basically removes all the unnecessary spaces

print(len(text)) # len of a string, self-explainatory

print(text.lower()) # every letters are put to low case
print(text.upper()) # //    //      //  //  // upper case

print(text.split('.')) # it creates a list with all of the words, separated by .; ex: hello.tim -> ["hello", "tim"]

##################################################

# slice operator for lists and strings
fruits = ["apple", "banana", "mango"]
text2 = "Hello i like python"

print(text2[:5]) # start at : stop at :
print(text[2:])
print(text[::2]) # every 2 letters

fruits.insert(1, "Blueberry") # the difference from append is that here you can decide where to add it
print(fruits, "\n")
fruits[2:2] = 'b'
print(fruits)