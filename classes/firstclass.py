class Dog(object):
    # constructor method
    # init is a must, this is automatic going to happen
    # self is basically the instance that is being created
    def __init__(self, name):
        # attribute
        self.name = name

    def speak(self):
        print("Hello, i'm", self.name) # that's why here we will see manu

    def change_name(self, name):
        self.name = name

    def add_weight(self, weight):
        self.weight = weight

# into self is automatically passed manu, the instance
# so if i set self.name = name i'm basically saying manu.name = name(the parameter)
manu = Dog("Manu") 
manu.speak()
manu.change_name("Manu")
manu.add_weight(65)
print(manu.weight)
print(manu.name)